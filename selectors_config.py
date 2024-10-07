# Selectors Dictionary for Web Scraping

site_selectors = {
    'books.toscrape.com': {  # Configuration for the books.toscrape.com site
        'item_selector': 'article.product_pod',  # Selector for the product item
        'title_selector': 'h3 a',  # Selector for the product title
        'price_selector': 'p.price_color',  # Selector for the product price
        'availability_selector': 'p.instock.availability',  # Selector for availability status
        'pagination_format': 'http://books.toscrape.com/catalogue/page-{}.html'  # Format for pagination URLs
    },
    'quotes.toscrape.com': {  # Configuration for the quotes.toscrape.com site
        'item_selector': 'div.quote',  
        'title_selector': 'span.text',  
        'price_selector': 'small.author',  
        'availability_selector': 'a.tag',  
        'pagination_format': 'http://quotes.toscrape.com/page/{}/'  
    }
}
