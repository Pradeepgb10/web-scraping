import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'QuotesSpider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']
    
    def parse(self, response):
        pass
