#!/usr/bin/env python3
"""Validate the public-safe Chapter 5 data archive using only the Python standard library."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path
from zipfile import ZipFile, BadZipFile

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / "05_quality_assurance"

checks: list[tuple[str, bool, str]] = []

def add(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, bool(ok), detail))

def count_csv(rel: str) -> int:
    path = ROOT / rel
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return max(0, sum(1 for _ in csv.reader(handle)) - 1)

# Required and prohibited paths
required = [
    "README.md",
    "CITATION.cff",
    "LICENSE_NOTICE.md",
    "LICENSE_DATA_CC_BY_4.0.md",
    "LICENSE_CODE_MIT.txt",
    "PUBLIC_RELEASE_AUDIT.md",
    "DATA_DICTIONARY.md",
    "03_scripts/R/run_all_chapter5.R",
    "02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv",
    "02_processed_outputs/section_5_3_relational_coordination/relational_network_edges_q90.csv",
    "02_processed_outputs/section_5_3_relational_coordination/relational_network_node_metrics_q90.csv",
    "02_processed_outputs/section_5_4_functional_differentiation/regulatory_delivery_scores_all_48_igos.csv",
    "02_processed_outputs/section_5_4_functional_differentiation/functional_alignment_scores_all_48_igos.csv",
    "05_quality_assurance/workbook_sanitisation_report.csv",
    "05_quality_assurance/analytical_invariance_check.csv",
    "05_quality_assurance/checksums_sha256.txt",
]
for rel in required:
    add(f"required:{rel}", (ROOT / rel).is_file())

prohibited = [
    "00_documentation/archive_notes/chapter5_marked_or_working_draft_reference.docx",
    "00_documentation/archive_notes/literature_and_concept_notes_1.txt",
    "00_documentation/archive_notes/literature_and_concept_notes_2.txt",
    "00_documentation/archive_notes/literature_and_concept_notes_3.txt",
]
for rel in prohibited:
    add(f"absent:{rel}", not (ROOT / rel).exists())

# Core record counts
expected_counts = {
    "02_processed_outputs/section_5_2_institutional_incongruence/dyadic_mandate_relational_similarity.csv": 1128,
    "02_processed_outputs/section_5_2_institutional_incongruence/figure_5_3_retained_mandate_overlap_edges.csv": 113,
    "02_processed_outputs/section_5_3_relational_coordination/relational_network_edges_q90.csv": 113,
    "02_processed_outputs/section_5_3_relational_coordination/relational_network_node_metrics_q90.csv": 48,
    "02_processed_outputs/section_5_4_functional_differentiation/regulatory_delivery_scores_all_48_igos.csv": 48,
    "02_processed_outputs/section_5_4_functional_differentiation/functional_alignment_scores_all_48_igos.csv": 48,
    "02_processed_outputs/section_5_4_functional_differentiation/functional_orientation_classes_all_48_igos.csv": 48,
}
for rel, expected in expected_counts.items():
    observed = count_csv(rel)
    add(f"count:{rel}", observed == expected, f"observed={observed}; expected={expected}")

# DOCX comments and tracked changes
for path in sorted(ROOT.rglob("*.docx")):
    rel = path.relative_to(ROOT).as_posix()
    try:
        with ZipFile(path) as zf:
            names = set(zf.namelist())
            comments = 0
            if "word/comments.xml" in names:
                text = zf.read("word/comments.xml").decode("utf-8", "ignore")
                comments = len(re.findall(r"<w:comment\b", text))
            document = zf.read("word/document.xml").decode("utf-8", "ignore") if "word/document.xml" in names else ""
            tracked = sum(len(re.findall(tag, document)) for tag in [
                r"<w:ins\b", r"<w:del\b", r"<w:moveFrom\b", r"<w:moveTo\b"
            ])
            add(f"docx-clean:{rel}", comments == 0 and tracked == 0,
                f"comments={comments}; tracked_change_elements={tracked}")
    except BadZipFile:
        add(f"docx-valid:{rel}", False, "Invalid DOCX package")

# XLSX public-safety checks
for path in sorted(ROOT.rglob("*.xlsx")):
    rel = path.relative_to(ROOT).as_posix()
    try:
        with ZipFile(path) as zf:
            names = zf.namelist()
            workbook = zf.read("xl/workbook.xml").decode("utf-8", "ignore")
            sheets = re.findall(r'<sheet[^>]*name="([^"]+)"', workbook)
            comments = sum(1 for n in names if n.startswith("xl/comments") and n.endswith(".xml"))
            threaded = sum(1 for n in names if "threadedComments" in n)
            external = sum(1 for n in names if n.startswith("xl/externalLinks/") and n.endswith(".xml"))
            ok = "Traceability_Long" not in sheets and comments == 0 and threaded == 0 and external == 0
            add(f"xlsx-public-safe:{rel}", ok,
                f"sheets={sheets}; comments={comments + threaded}; external_links={external}")
    except (BadZipFile, KeyError):
        add(f"xlsx-valid:{rel}", False, "Invalid XLSX package")

# Sanitisation and invariance reports
with (QA / "workbook_sanitisation_report.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
add("workbook-sanitisation:8-files", len(rows) == 8, f"observed={len(rows)}")
add("workbook-sanitisation:matrix-values", all(r.get("matrix_values_identical") == "True" for r in rows))

with (QA / "analytical_invariance_check.csv").open(newline="", encoding="utf-8") as handle:
    inv = list(csv.DictReader(handle))
add("analytical-invariance:all-pass",
    bool(inv) and all(r.get("analytical_content_identical") == "TRUE" for r in inv),
    f"checks={len(inv)}")

# Publication-neutral metadata and final licence
citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
add("citation:dataset-type", "type: dataset" in citation)
add("citation:publication-neutral",
    not re.search(r"thesis supplementary|doctoral thesis|PhD thesis", citation, re.I))

licence = (ROOT / "LICENSE_NOTICE.md").read_text(encoding="utf-8")
add("licence:finalised",
    "CC BY 4.0" in licence and "MIT License" in licence and
    "Before public release" not in licence)

# Personal editorial names must not occur in distributed text or OOXML packages
personal_names = re.compile(r"\b(Michelle Voyer|Rachel|Alistair)\b", re.I)
name_hits: list[str] = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT).as_posix()
    if rel == "05_quality_assurance/validate_public_archive.py":
        continue
    if path.suffix.lower() in {".md", ".txt", ".csv", ".json", ".cff", ".r", ".py"}:
        if personal_names.search(path.read_text(encoding="utf-8", errors="ignore")):
            name_hits.append(rel)
    elif path.suffix.lower() in {".docx", ".xlsx"}:
        try:
            with ZipFile(path) as zf:
                for member in zf.namelist():
                    if member.endswith((".xml", ".rels", ".txt")):
                        if personal_names.search(zf.read(member).decode("utf-8", "ignore")):
                            name_hits.append(f"{rel}:{member}")
                            break
        except BadZipFile:
            pass
add("personal-editorial-names:absent", not name_hits, "; ".join(name_hits[:10]))

# Archive hygiene
hygiene_bad = [
    p.relative_to(ROOT).as_posix()
    for p in ROOT.rglob("*")
    if p.name in {".DS_Store", "Thumbs.db"} or "__MACOSX" in p.parts or p.name.startswith("._")
]
add("archive-hygiene", not hygiene_bad, "; ".join(hygiene_bad[:10]))

# Checksum verification
checksum_file = QA / "checksums_sha256.txt"
checksum_failures: list[str] = []
if checksum_file.exists():
    for line in checksum_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, rel = line.split("  ", 1)
        path = ROOT / rel
        if not path.is_file():
            checksum_failures.append(f"missing:{rel}")
            continue
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            checksum_failures.append(f"mismatch:{rel}")
add("checksums", not checksum_failures, "; ".join(checksum_failures[:10]))

# Report
passed = sum(ok for _, ok, _ in checks)
failed = len(checks) - passed
print(f"Chapter 5 public archive validation: {passed}/{len(checks)} checks passed")
for name, ok, detail in checks:
    if not ok:
        print(f"FAIL: {name}" + (f" — {detail}" if detail else ""))
if failed:
    sys.exit(1)
