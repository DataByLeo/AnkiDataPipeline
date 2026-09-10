"""
Loads data into Anki using the AnkiConnect API.
"""

import os
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()


def load_data_from_google_sheets():
    # Initialize the Google Sheets client
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    credentials_dict = {
    "type": "service_account",
    "project_id": os.environ.get("GCP_PROJECT_ID"),
    "client_email": os.environ.get("GCP_CLIENT_EMAIL"),
    "private_key": os.environ.get("GCP_PRIVATE_KEY").replace("\\n", "\n"), # Fixes newline formatting
    "token_uri": "https://oauth2.googleapis.com/token",
    }
    
    creds = Credentials.from_service_account_info(credentials_dict, scopes=scope)
    client = gspread.authorize(creds)

    spreadsheet_id = os.environ.get("GOOGLE_SPREADSHEET_ID")
    if not spreadsheet_id:
        raise ValueError("Error: GOOGLE_SPREADSHEET_ID environment variable is not set")

    # Open the Google Sheet
    sheet = client.open_by_key(spreadsheet_id).sheet1

    # Load data into a DataFrame
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df


def main():
    df = load_data_from_google_sheets()
    print("Data loaded from Google Sheets:")
    print(df.head())  # Print the first few rows of the DataFrame
    # Do something with the loaded data, e.g., upload to Anki

if __name__ == "__main__":
    main()
