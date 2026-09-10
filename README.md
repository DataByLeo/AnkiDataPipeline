# 2 Stage ETL Vocabulary Pipeline

**Source**: Google Sheets

Destination: Anki

---

### Stage 1 Extract (extract_sheets.py):

Get Data from Sheets

### Stage 2 Transform & Load (load_anki.py):
Apply Changes/Transformations from Stage 1
Load into Anki


## Setup
### Prerequisites:


Deployment Steps
Copy .env.example to a new file named .env and fill in your unique Google Spreadsheet ID.

### Run Pipeline
```
# Execute Stage 1
python extract_sheets.py

# Execute Stage 2
python load_anki.py
```