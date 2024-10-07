import requests
from bs4 import BeautifulSoup
from selectors_config import site_selectors
from dynamic_scraper import scrape_dynamic_site
from data_processing import insert_valid_data, log_invalid_data
from google_sheet_reader import authenticate_google_sheets, fetch_urls_and_advertisers
from sites_config import dynamic_sites
from urllib.parse import urlparse

# Function to check if the URL is active
def is_url_active(url):
    try:
        response = requests.head(url, timeout=30)  # Send a HEAD request to the URL
        return response.status_code in [200, 301, 302]  # Check if the status code indicates a valid response
    except requests.RequestException:
        return False  # Return False if there's an exception

# Function to determine if the site is dynamic
def is_dynamic_site(url, dynamic_sites_config):
    domain = urlparse(url).netloc  # Parse the domain from the URL
    site_info = dynamic_sites_config.get(domain)  # Check if the domain is in the dictionary

    if site_info:
        return site_info.get('is_dynamic', False)  # Return True if it's dynamic, otherwise False
    return False  # Return False if the site is not configured

# Function to obtain selectors based on the site
def get_selectors(url):
    domain = urlparse(url).netloc  # Extract the domain from the URL
    if domain in site_selectors:
        return site_selectors[domain]  # Return the selectors for the specified domain
    else:
        raise ValueError(f"Selectors not configured for site: {domain}")  # Raise an error if not configured

# Function for scraping static sites (requests + BeautifulSoup)
def scrape_static_site(url):
    selectors = get_selectors(url)  # Get the selectors for the site
    response = requests.get(url, timeout=10)  # Send a GET request to the URL
    soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content
    
    items = soup.select(selectors['item_selector'])  # Select items using the specified selector
    scraped_data = []  # Initialize a list to hold the scraped data
    
    for item in items:
        # Extract the title, price, and availability using the defined selectors
        title_element = item.select_one(selectors['title_selector'])
        title = title_element['title'] if title_element and 'title' in title_element.attrs else title_element.get_text(strip=True) if title_element else 'N/A'
        
        price_element = item.select_one(selectors['price_selector'])
        price = price_element.get_text(strip=True) if price_element else 'N/A'
        
        availability_element = item.select_one(selectors['availability_selector'])
        availability = availability_element.get_text(strip=True) if availability_element else 'N/A'

        # Append the scraped data to the list
        scraped_data.append({
            'URL': url,
            'Title': title,
            'Price': price,
            'Availability': availability
        })
    return scraped_data  # Return the list of scraped data

# Function for scraping multiple pages
def scrape_multiple_pages(base_url, domain, pages=10):
    selectors = get_selectors(base_url)  # Get the selectors for pagination
    pagination_format = selectors.get('pagination_format')  # Get the pagination format
    
    if not pagination_format:
        raise ValueError(f"Pagination format not configured for site: {domain}")  # Raise an error if pagination is not configured
    
    all_data = []  # Initialize a list to hold all scraped data
    
    for page_num in range(1, pages + 1):  # Loop through the specified number of pages
        url = pagination_format.format(page_num)  # Format the URL for the current page
        print(f"Scraping page {page_num}: {url}")  # Print the current page being scraped
        page_data = scrape_static_site(url)  # Scrape the current page
        all_data.extend(page_data)  # Add the scraped data to the list
    
    return all_data  # Return all scraped data

# Function to validate scraped data
def validate_scraped_data(scraped_data):
    required_fields = ['Title', 'Price', 'Availability']  # Define the required fields
    for item in scraped_data:
        for field in required_fields:
            if field not in item or not item[field]:  # Check if the field is missing or empty
                return False, item  # Return False and the invalid item
    return True, None  # Return True if all data is valid

# Main scraping function
def scrape_data(url, page_limit=10):
    try:
        # Check if the site is dynamic or static
        if is_dynamic_site(url, dynamic_sites):
            print(f"Scraping dynamic content from {url}")
            return scrape_dynamic_site(url)  # Call the function for scraping dynamic sites
        else:
            print(f"Scraping static content from {url}")
            domain = urlparse(url).netloc
            return scrape_multiple_pages(url, domain, pages=page_limit)  # Call the function for scraping static sites
    except Exception as e:
        print(f"Error scraping {url}: {e}")  # Log any errors encountered
        return []  # Return an empty list on error

# Function to log errors for inactive URLs
def log_inactive_url(advertiser_name, url, error_message, sheet):
    sheet.append_row([advertiser_name, url, error_message])  # Log the inactive URL in the sheet

# Main function to execute the complete process
def main():
    # Configure the path to the credentials
    credentials_path = '/home/henrique-tardoqui/Downloads/rakuten-test-437701-ec863dca066c.json'

    # Fetch URLs and advertisers from Google Sheets
    spreadsheet_id = '1LtnX5Yu8dgHYXbC-4zlpvPSIV9TYqQ7sVYsovC03FXs'
    urls_data = fetch_urls_and_advertisers(spreadsheet_id, 'Advertisers List', credentials_path)
    
    # Open sheets for recording data and errors
    client = authenticate_google_sheets(credentials_path)
    
    inactive_urls_sheet = client.open_by_key(spreadsheet_id).worksheet('Inactive URLs')
    scraping_results_sheet = client.open_by_key(spreadsheet_id).worksheet('Scraping Results')
    scraping_report_sheet = client.open_by_key(spreadsheet_id).worksheet('Scraping Report')

    total_urls = len(urls_data)  # Get the total number of URLs
    total_scraped = 0  # Initialize a counter for scraped data
    total_errors = 0  # Initialize a counter for errors
    
    for entry in urls_data:
        url = entry['URL']  # Extract the URL
        advertiser_name = entry['Advertiser Name']  # Extract the advertiser's name
        
        if is_url_active(url):  # Check if the URL is active
            scraped_data = scrape_data(url)  # Scrape the data from the URL
            is_valid, invalid_data = validate_scraped_data(scraped_data)  # Validate the scraped data
            
            if is_valid:
                insert_valid_data(scraped_data, scraping_results_sheet, advertiser_name)
                total_scraped += len(scraped_data)  # Update the total scraped count
            else:
                log_invalid_data(advertiser_name, url, "Invalid data structure", scraping_results_sheet)  # Log invalid data
                total_errors += 1  # Increment the error count
        else:
            log_inactive_url(advertiser_name, url, "URL not active", inactive_urls_sheet)  # Log inactive URLs
            total_errors += 1  # Increment the error count
    
    # Generate the final report
    scraping_report_sheet.append_row([f"Total URLs Processed: {total_urls}"])
    scraping_report_sheet.append_row([f"Total Data Scraped: {total_scraped}"])
    scraping_report_sheet.append_row([f"Total Errors: {total_errors}"])

if __name__ == "__main__":
    main()  # Execute the main function
