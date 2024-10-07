import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets(credentials_path):
    """
    Authenticate to Google Sheets using service account credentials.

    Args:
        credentials_path (str): Path to the service account JSON keyfile.

    Returns:
        client: Authorized gspread client.
    """
    # Define the scope for Google Sheets and Google Drive access
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # Load credentials from the JSON keyfile
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    
    # Authorize the client with the credentials
    client = gspread.authorize(creds)
    return client

# Function to fetch URLs and advertiser names from Google Sheets
def fetch_urls_and_advertisers(spreadsheet_id, sheet_range, credentials_path):
    """
    Fetch URLs and advertiser names from a specified Google Sheets worksheet.

    Args:
        spreadsheet_id (str): ID of the Google Sheets document.
        sheet_range (str): The name of the worksheet to fetch data from.
        credentials_path (str): Path to the service account JSON keyfile.

    Returns:
        list: List of dictionaries containing URLs and advertiser names.
    """
    #Authenticate
    client = authenticate_google_sheets(credentials_path)
    
    # Open the specified worksheet
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_range)
    
    # Get all records from the worksheet
    data = sheet.get_all_records()
    return data
