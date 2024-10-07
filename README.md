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


**To run the scraper, execute the following command in the terminal:**
python scraper.py
