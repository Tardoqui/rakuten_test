from datetime import datetime

# Function to save valid scraped data to Google Sheets
def insert_valid_data(scraped_data, sheet, advertiser_name):
    # Create a list to hold the rows for insertion
    rows_to_insert = []
    
    # Loop through each scraped item and format it for insertion
    for item in scraped_data:
        # Prepare a row with data in the correct order:
        # Advertiser Name, Ad Title, Ad Description, Product, Price, Date Scraped, Ad Image, Remarks
        row = [
            advertiser_name,             # Advertiser Name
            item['Title'],               # Ad Title (scraped title)
            'N/A',                       # Ad Description (not scraped, set as 'N/A' or another placeholder)
            item['Title'],               # Product (assume it’s the same as title, adjust as needed)
            item['Price'],               # Price (scraped price)
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Date Scraped (current timestamp)
            'N/A',                       # Ad Image (not scraped, set as 'N/A' or another placeholder)
            item['Availability']         # Remarks (use the availability as remarks)
        ]
        rows_to_insert.append(row)  # Add the row to the list
    
    # Add all rows to the sheet in one operation
    sheet.append_rows(rows_to_insert, value_input_option='RAW')



# Function to log errors for invalid data in Google Sheets
def log_invalid_data(advertiser_name, url, error_message, sheet):
    # Append a row with the advertiser's name, URL, and error message
    sheet.append_row([advertiser_name, url, error_message])
