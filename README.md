# Web Scraping Project Documentation
**(Version 1.0)**

## Overview
This project, now at Version 1.0, automates web scraping for both static and dynamic websites using tools like requests, BeautifulSoup, and Selenium. Developed with the tools available at the moment, this solution demonstrates the feasibility of web scraping within the constraints of current resources.

The project is designed with scalability in mind, allowing for easy updates as new requirements arise. It could also be implemented in an RPA tool like Automation Anywhere, following the same conditions and rules established in the code. While the core functionality is complete, additional work can further optimize this project. With more time, a fully comprehensive version addressing all aspects of scraping automation could be developed.

## Key Features
- **Dynamic and Static Site Scraping:** Supports different types of content with appropriate tools (BeautifulSoup for static, Selenium for dynamic).
- **Data Validation:** Ensures all scraped data meets predefined standards before insertion.
- **Google Sheets Integration:** Scraped data is logged directly into Google Sheets for easy access and review.
- **Pagination Support:** Automatically scrapes multiple pages of content for larger data sets.
- **Scalability:** The architecture is designed to easily incorporate new features, handle new site types, and maintain code efficiency as requirements grow.

## Installation

### 1. Clone the Repository:

git clone https://github.com/Tardoqui/rakuten_test.git
cd rakuten_test

### 2. Install Dependencies:

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


**Next, install the required libraries by running:**
pip install -r requirements.txt


**3. Set Up Google Sheets API:**
Create a project in the Google Developers Console.
Enable the Google Sheets API.
Create a service account and download the JSON credentials file.
Share your Google Sheets with the service account email.

**4. Configure Chromedriver:**
Download and install Chromedriver and ensure it's in your PATH or provide the path in dynamic_scraper.py.


**MODULES:**

**scraper.py**
Description: Contains functions for scraping data from websites.
Key Functions:
is_url_active(url): Checks if the given URL is accessible.
is_dynamic_site(url): Determines if the site requires Selenium for scraping.
scrape_static_site(url): Extracts data from static pages using requests and BeautifulSoup.
scrape_dynamic_site(url): Extracts data from dynamic pages using Selenium.
validate_scraped_data(scraped_data): Validates the structure of the scraped data.
main(): Orchestrates the entire scraping process, managing data collection and error logging.

**selectors_config.py**
Description: Contains a dictionary that maps website domains to their respective CSS selectors used in scraping.
Key Elements:
site_selectors: A dictionary holding the selectors for each site.


**google_sheet_reader.py**
Description: Handles authentication and data retrieval from Google Sheets.
Key Functions:
authenticate_google_sheets(credentials_path): Authenticates using service account credentials.
fetch_urls_and_advertisers(spreadsheet_id, sheet_range, credentials_path): Fetches URLs and advertiser names from the specified Google Sheets.


**dynamic_scraper.py**
Description: Utilizes Selenium to scrape content from dynamically loaded websites.
Key Functions:
scrape_dynamic_site(url): Navigates to the URL using Selenium and extracts the relevant data.

**data_processing.py**
Description: Manages the insertion of valid data and logging of invalid data into Google Sheets.
Key Functions:
insert_valid_data(scraped_data, sheet): Inserts valid scraped data into Google Sheets.
log_invalid_data(advertiser_name, url, error_message, sheet): Logs invalid data attempts for later review.

**sites_config.py**
Description: Stores a dictionary of dynamic and static websites, helping the scraper distinguish between static and dynamic content loading.
Key Elements:
dynamic_sites: A dictionary that specifies whether a site is dynamic and provides additional information about it. The scraper uses this dictionary to decide whether to use requests/BeautifulSoup for static sites or Selenium for dynamic sites.




**To run the scraper, execute the following command in the terminal:**

python scraper.py
