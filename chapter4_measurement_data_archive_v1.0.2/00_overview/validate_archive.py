#!/usr/bin/env python3
"""Validate the public-safe Chapter 4 measurement archive.

Run from any location:
    python 00_overview/validate_archive.py
"""
from pathlib import Path
import csv
import gzip
import hashlib
import sys

def read_csv_rows(path, gz=False):
    opener = gzip.open if gz or str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8-sig", newline="") as f:
        r=csv.reader(f)
        header=next(r,[])
        rows=list(r)
    return header, rows


def matrix_stats(path):
    h, rows=read_csv_rows(path)
    missing=sum(1 for row in rows for v in row if (v is None or str(v).strip()==""))
    return len(rows), len(h), missing, h, rows


def collect_checks(rootp):
    checks=[]
    def add(name, observed, expected, status=None, note=""):
        if status is None:
            status = "PASS" if str(observed)==str(expected) else "FAIL"
        checks.append({"check":name,"observed":observed,"expected":expected,"status":status,"note":note})
    # roster
    h,rows=read_csv_rows(rootp/"01_study_population/data/ch04_s1_igo_roster_48.csv")
    add("Study roster rows",len(rows),48)
    ids=[r[0] for r in rows]
    add("Unique IGO identifiers",len(set(ids)),48)
    # source register
    h,srows=read_csv_rows(rootp/"02_document_corpus/data/processed/ch04_s2_public_source_register_58.csv")
    add("Public source register rows",len(srows),58)
    idx={x:i for i,x in enumerate(h)}
    included=sum(1 for r in srows if r[idx["public_file_included"]].strip().lower()=="yes")
    add("Third-party source files marked included",included,0)
    url_blank=sum(1 for r in srows if not r[idx["source_url"]].strip())
    date_blank=sum(1 for r in srows if not r[idx["access_date"]].strip())
    add("Blank source_url fields",url_blank,58,"PASS" if url_blank==58 else "INFO","Reported as preserved metadata gap; no values inferred.")
    add("Blank access_date fields",date_blank,58,"PASS" if date_blank==58 else "INFO","Reported as preserved metadata gap; no values inferred.")
    # file types
    files=[p for p in rootp.rglob("*") if p.is_file()]
    third_party=[p for p in files if p.suffix.lower() in {".pdf",".doc"}]
    add("Institutional PDF/DOC payload files",len(third_party),0)
    # corpus indices
    h,rows=read_csv_rows(rootp/"02_document_corpus/data/interim/ch04_s2_page_index_public_2435.csv.gz",True)
    add("Public page-index records",len(rows),2435)
    add("Page-index extracted-text columns",sum(1 for x in h if x.lower() in {"text","page_text","extracted_text"}),0)
    h,rows=read_csv_rows(rootp/"02_document_corpus/data/interim/ch04_s2_paragraph_index_public_5159.csv.gz",True)
    add("Public paragraph-index records",len(rows),5159)
    add("Paragraph-index para_text column",1 if "para_text" in h else 0,0)
    h,rows=read_csv_rows(rootp/"02_document_corpus/data/interim/ch04_s2_extraction_log_130.csv")
    add("Extraction-log records",len(rows),130)
    # step3 public indexes
    specs=[
        ("Candidate review index","03_attribute_coding_clean_review/data/ch04_s3_candidate_review_index_public_3636.csv",3636,{"source_title","excerpt_<=50w"}),
        ("Decision log index","03_attribute_coding_clean_review/data/ch04_s3_decision_log_public_3676.csv",3676,{"source_title","excerpt_<=50w","matrix_cell_text_full"}),
        ("Traceability index","03_attribute_coding_clean_review/data/ch04_s3_traceability_index_public_3074.csv",3074,{"source_title","excerpt_<=50w","matrix_cell_text_full","excerpt_full"}),
    ]
    for label,rel,n,forbidden in specs:
        h,rows=read_csv_rows(rootp/rel)
        add(f"{label} records",len(rows),n)
        present=sorted(forbidden.intersection(h))
        add(f"{label} withheld-text columns present",len(present),0,note="; ".join(present))
    # baseline
    r,c,m,h,rows=matrix_stats(rootp/"04_attribute_matrix_integration/data/ch04_s4_baseline_attribute_matrix_wide_48x10.csv")
    add("Baseline matrix rows",r,48)
    add("Baseline matrix columns including identifier",c,11,note="Nine substantive attributes plus auxiliary Scale and Institution identifier.")
    add("Unique baseline organisations",len(set(x[0] for x in rows)),48)
    substantive_missing=sum(1 for row in rows for v in row[1:] if not str(v).strip())
    add("Blank baseline attribute fields",substantive_missing,0)
    r,c,m,h,rows=matrix_stats(rootp/"04_attribute_matrix_integration/data/ch04_s4_baseline_attribute_matrix_long_480.csv")
    add("Baseline long-form cells",r,480)
    h,rows=read_csv_rows(rootp/"04_attribute_matrix_integration/data/ch04_s4_orphan_evidence.csv")
    add("Orphan evidence records",len(rows),0)
    # schema/activation
    h,rows=read_csv_rows(rootp/"05_category_schema/data/ch04_s5_category_schema_80_reconciled.csv")
    add("Category schema rows",len(rows),80)
    r,c,m,h,rows=matrix_stats(rootp/"05_category_schema/data/ch04_s5_category_activation_matrix_48x80.csv")
    add("Category activation rows",r,48)
    add("Category activation columns including identifier",c,81)
    activ=0
    for row in rows:
        for v in row[1:]:
            try: activ += 1 if float(v)==1 else 0
            except: pass
    add("CLEAN-confirmed category activations",activ,1862)
    # score matrices
    for label,rel in [
        ("Hybrid score","06_scoring_and_normalisation/outputs/ch04_s6_hybrid_score_matrix_48x80.csv"),
        ("Within-IGO","06_scoring_and_normalisation/outputs/ch04_s6_within_igo_matrix_48x80.csv"),
        ("Across-IGO","06_scoring_and_normalisation/outputs/ch04_s6_across_igo_matrix_48x80.csv"),
    ]:
        r,c,m,h,rows=matrix_stats(rootp/rel)
        add(f"{label} matrix rows",r,48)
        add(f"{label} matrix columns including identifier",c,81)
        add(f"{label} matrix missing cells",m,0)
        if label!="Hybrid score":
            vals=[]
            for row in rows:
                for v in row[1:]:
                    try: vals.append(float(v))
                    except: pass
            ok = bool(vals) and min(vals)>=-1e-9 and max(vals)<=10+1e-9
            add(f"{label} matrix range",f"{min(vals):.6g} to {max(vals):.6g}","0 to 10","PASS" if ok else "FAIL")
    # master
    r,c,m,h,rows=matrix_stats(rootp/"07_analysis_ready_outputs/ch04_master_matrix_48x174_corrected.csv")
    add("Corrected master-matrix rows",r,48)
    add("Corrected master-matrix columns",c,174)
    add("Corrected master-matrix missing cells",m,0)
    # descriptions
    for label,rel,n in [
        ("Descriptive family-summary","07_analysis_ready_outputs/descriptive_summary/ch04_family_summary.csv",8),
        ("Descriptive category-summary","07_analysis_ready_outputs/descriptive_summary/ch04_category_prevalence.csv",80),
        ("Descriptive IGO-summary","07_analysis_ready_outputs/descriptive_summary/ch04_igo_overall_profiles.csv",48),
    ]:
        h,rows=read_csv_rows(rootp/rel); add(f"{label} rows",len(rows),n)
    add("Descriptive IGO-profile plot",1 if (rootp/"07_analysis_ready_outputs/descriptive_summary/ch04_igo_overall_profile_plot.png").exists() else 0,1)
    # release exclusions
    h,rows=read_csv_rows(rootp/"00_overview/removed_files_public_release.csv")
    add("Public-release removal-register rows",len(rows),96)
    old_names=[
        "02_document_corpus/data/interim/ch04_s2_corpus_pages_2435.csv.gz",
        "02_document_corpus/data/interim/ch04_s2_corpus_paragraphs_5159.csv.gz",
        "03_attribute_coding_clean_review/data/ch04_s3_candidate_review_queue_3636.csv",
        "03_attribute_coding_clean_review/data/ch04_s3_decision_log.csv",
        "03_attribute_coding_clean_review/data/ch04_s3_traceability_long_file_3074.csv",
        "03_attribute_coding_clean_review/outputs/tables/ch04_s3_attribute_coding_bundle.xlsx",
    ]
    present=sum(1 for rel in old_names if (rootp/rel).exists())
    add("Named evidence-rich legacy files present",present,0)
    family_trace=len(list((rootp/"06_scoring_and_normalisation/outputs/family_csvs").glob("*_traceability_long_corrected.csv")))
    family_wb=len(list((rootp/"06_scoring_and_normalisation/outputs/family_workbooks").glob("*.xlsx"))) if (rootp/"06_scoring_and_normalisation/outputs/family_workbooks").exists() else 0
    add("Scoring traceability-long CSVs present",family_trace,0)
    add("KWIC-bearing family workbooks present",family_wb,0)
    # raw/clean text xlsx
    disallowed_raw=[]
    for sub in ["06_scoring_and_normalisation/data/raw","06_scoring_and_normalisation/data/clean"]:
        for p in (rootp/sub).glob("*.xlsx"):
            if p.name!="ch04_s6_raw_year_of_establishment_with_context.xlsx":
                disallowed_raw.append(p)
    add("Text-bearing RAW/CLEAN workbooks present",len(disallowed_raw),0)
    # required notices
    req=[
        "PUBLIC_RELEASE_AUDIT.md","RIGHTS_AND_REUSE.md","LICENSE.md",
        "02_document_corpus/data/raw/igo_documents/SOURCE_DOCUMENTS_NOT_INCLUDED.md",
        "02_document_corpus/data/interim/README_PUBLIC_SAFE.md",
        "03_attribute_coding_clean_review/data/README_PUBLIC_SAFE.md",
        "06_scoring_and_normalisation/data/README_PUBLIC_SAFE.md",
    ]
    add("Required public-release notices",sum(1 for x in req if (rootp/x).exists()),len(req))
    # hygiene
    bad=[]
    for p in files:
        rel=str(p.relative_to(rootp))
        if "__MACOSX" in rel or p.name==".DS_Store" or p.name.startswith("~$") or "/.git/" in "/"+rel:
            bad.append(rel)
    add("Archive hygiene exceptions",len(bad),0,note="; ".join(bad[:10]))
    return checks


def verify_checksums(rootp):
    register = rootp / "CHECKSUMS_SHA256.csv"
    if not register.exists():
        return [("Checksum register present", "No", "Yes", "FAIL", "")]
    results = []
    with open(register, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    bad = []
    missing = []
    for row in rows:
        rel = row["relative_path"]
        p = rootp / rel
        if not p.exists():
            missing.append(rel)
            continue
        h = hashlib.sha256()
        with open(p, "rb") as src:
            for chunk in iter(lambda: src.read(1024 * 1024), b""):
                h.update(chunk)
        if h.hexdigest() != row["sha256"]:
            bad.append(rel)
    results.append(("Checksum-register entries", len(rows), len(rows), "PASS", ""))
    results.append(("Checksum missing files", len(missing), 0, "PASS" if not missing else "FAIL", "; ".join(missing[:10])))
    results.append(("Checksum mismatches", len(bad), 0, "PASS" if not bad else "FAIL", "; ".join(bad[:10])))
    return results

def main():
    rootp = Path(__file__).resolve().parents[1]
    checks = collect_checks(rootp)
    for name, observed, expected, status, note in verify_checksums(rootp):
        checks.append({"check": name, "observed": observed, "expected": expected, "status": status, "note": note})
    width = max(len(c["check"]) for c in checks)
    for c in checks:
        print(f'{c["status"]:4s}  {c["check"]:<{width}}  observed={c["observed"]} expected={c["expected"]}'
              + (f'  {c["note"]}' if c["note"] else ""))
    failed = [c for c in checks if c["status"] == "FAIL"]
    print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
