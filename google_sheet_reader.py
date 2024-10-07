import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate to Google Sheets using service account credentials
def authenticate_google_sheets(credentials_path):
    # Define the scope for Google Sheets and Google Drive access
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # Load credentials from the JSON keyfile
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    
    # Authorize the client with the credentials
    client = gspread.authorize(creds)
    return client

# Function to fetch URLs and advertiser names from Google Sheets
def fetch_urls_and_advertisers(spreadsheet_id, sheet_range, credentials_path):
    # Authenticate to Google Sheets
    client = authenticate_google_sheets(credentials_path)
    
    # Open the specified worksheet using the spreadsheet ID and range
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_range)
    
    # Get all records (rows) from the worksheet
    data = sheet.get_all_records()
    return data
