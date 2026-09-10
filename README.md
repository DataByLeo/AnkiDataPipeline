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

#### Private Sheet connection via GitHub Secrets:
This methods utilizies the Github Secrets, to avoid using a json file in the project.
1. Google Cloud Setup:
1.1 Create or select project
https://console.cloud.google.com/

1.2 Enable Google Sheets API
https://console.cloud.google.com/apis/library/sheets.googleapis.com?supportedpurview=project

1.3 Navigate to IAM & Admin > Service Accounts and click Create Service Account.
Only name skip Permissions + Principals

1.4 Click on newly created service account > Key > Add Key > Create New Key > select JSON
Will need from the downloaded file the client_email, project_id, private_key for next steps

2. Share Google Sheet
Go to Google Sheet > top right "Share" > Add client_email > Grant "Viewer" > Deselect "Notify People" > press Share

3.1 Configure Github Secrets via Actions #This is for automated workflows
Go to Repository > Settings (Not account Settings but Repo Settings) > Left Side Secrets and variables > Actions > Green "New repository secret"
3.2 Configure Github Secrets via Codespaces #This is for Manually executing via Codespaces
Go to Repository > Settings (Not account Settings but Repo Settings) > Left Side Secrets and variables > Codespaces > Green "New repository secret"

Add Secrets from previously JSON file, everything that is inside the corresponding "" of the secret:
client_email > GCP_CLIENT_EMAIL
project_id > GCP_PROJECT_ID
private_key > GCP_PRIVATE_KEY

3.3 Rebuild Codspaces, to pull Secrets into environment
Ctrl + Shift + P > Codespaces: Rebuild Container


#### Via Json File in Project

Deployment Steps
Copy .env.example to a new file named .env and fill in your unique Google Spreadsheet ID.

### Run Pipeline
pip3 install -r requirements.txt
```
# Execute Stage 1
python extract_sheets.py

# Execute Stage 2
python load_anki.py
```