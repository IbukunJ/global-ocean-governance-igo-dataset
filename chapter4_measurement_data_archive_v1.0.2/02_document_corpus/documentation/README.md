# Documentary corpus — public-safe edition

The complete research corpus comprised 58 official institutional documents, 2,435 page records, 5,159 paragraph units, and 130 logged extraction exceptions. The institutional documents and extracted text are not redistributed in this public edition.

The public corpus layer contains:

- `data/processed/ch04_s2_public_source_register_58.csv`: the canonical public provenance register;
- `data/processed/ch04_s2_document_manifest_58.csv`: the original researcher-facing document metadata;
- `data/processed/ch04_s2_document_extraction_summary_58.csv`;
- `data/interim/ch04_s2_page_index_public_2435.csv.gz`;
- `data/interim/ch04_s2_paragraph_index_public_5159.csv.gz`; and
- `data/interim/ch04_s2_extraction_log_130.csv`.

The public indexes retain stable identifiers, structural locators, character counts, and SHA-256 hashes but contain no page or paragraph text. The `data/raw/igo_documents/` folder contains only a retrieval notice.

The extraction scripts and environment files remain available to document the procedure. They require locally and lawfully reacquired source documents and should not be expected to run end-to-end against the public archive alone.
