# Dynamic Sites Configuration
# This dictionary identifies whether certain sites are dynamic or static,
# which dictates how they will be scraped.

dynamic_sites = {
    'dynamic-site.com': {
        'description': 'A site that requires dynamic content loading.',
        'is_dynamic': True
    },
    'quotes.toscrape.com': {
        'description': 'A Static site to be scraped with Beautiful Soap.',
        'is_dynamic': False
    },
    'books.toscrape.com': {
        'description': 'A static site that can be scraped without Selenium.',
        'is_dynamic': False
    }
}
