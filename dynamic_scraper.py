from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def scrape_dynamic_site(url):
    """
    Scrape data from a dynamic site using Selenium.

    Args:
        url (str): The URL of the dynamic site to scrape.

    Returns:
        list: A list of dictionaries containing scraped data from the dynamic site.
    """
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    
    # Navigate to the specified URL
    driver.get(url)
    
    # Wait implicitly for elements to be loaded
    driver.implicitly_wait(10)
    
    # Capture the HTML source after JavaScript has executed
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Define selectors for the dynamic content
    selectors = {
        'item_selector': '.dynamic-item',  # CSS selector for items
        'title_selector': '.title',         # CSS selector for titles
        'price_selector': '.price',         # CSS selector for prices
        'availability_selector': '.availability'  # CSS selector for availability
    }
    
    # Select all items based on the defined selector
    items = soup.select(selectors['item_selector'])
    scraped_data = []
    
    # Loop through each item and extract relevant data
    for item in items:
        title = item.select_one(selectors['title_selector']).get_text(strip=True) if item.select_one(selectors['title_selector']) else 'N/A'
        price = item.select_one(selectors['price_selector']).get_text(strip=True) if item.select_one(selectors['price_selector']) else 'N/A'
        availability = item.select_one(selectors['availability_selector']).get_text(strip=True) if item.select_one(selectors['availability_selector']) else 'N/A'
        
        # Append the extracted data to the scraped data list
        scraped_data.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })
    
    # Close the WebDriver session
    driver.quit()
    
    return scraped_data
