from datetime import datetime


def insert_valid_data(scraped_data, sheet, advertiser_name):
    """
    Save valid scraped data to Google Sheets.

    Args:
        scraped_data (list): List of valid scraped data dictionaries.
        sheet: Google Sheets worksheet to insert data.
        advertiser_name (str): Name of the advertiser related to the data.
    """
   
    rows_to_insert = []
    
    # Loop through each scraped item and format it for insertion
    for item in scraped_data:
        # Prepare a row with data in the correct order:
        # Advertiser Name, Ad Title, Ad Description, Product, Price, Date Scraped, Ad Image, Remarks
        row = [
            advertiser_name,             # Advertiser Name
            item['Title'],               # Ad Title (scraped title)
            'N/A',                        
            item['Title'],               # Product (assume it’s the same as title, adjust as needed)
            item['Price'],               # Price (scraped price)
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Date Scraped (current timestamp)
            'N/A',                       # Ad Image (not scraped, set as 'N/A' or another placeholder)
            item['Availability']         # Remarks (use the availability as remarks)
        ]
        rows_to_insert.append(row)  # Add the row to the list
    
    # Add all rows to the sheet in one operation
    sheet.append_rows(rows_to_insert, value_input_option='RAW')



def log_invalid_data(advertiser_name, url, error_message, sheet):
    """
    Log errors for invalid data in Google Sheets.

    Args:
        advertiser_name (str): Name of the advertiser.
        url (str): The URL associated with the invalid data.
        error_message (str): Message explaining the error.
        sheet: Google Sheets worksheet to log the error.
    """

    sheet.append_row([advertiser_name, url, error_message])
