#2 - input processors and item loaders
#3 - item pipelines 
import codecs
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader #2
from scrapy.loader.processors import TakeFirst #3

from books.items import BooksItem

class BookcrawlerSpider(CrawlSpider):
    name = 'BookCrawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=('catalogue/category')), callback='parsepage', follow=True),
    )

    def parsepage(self, res):
        bk = BooksItem()
        books = res.xpath('//article[@class="product_pod"]')

        for b in books:
            """ bk['title'] = b.xpath('.//h3/a/@title').extract_first()
            bk['price'] = b.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            bk['imageurl'] = self.start_urls[0] + b.xpath('.//img[@class="thumbnail"]/@src').extract_first().replace('../', '')
            bk['bookurl'] = self.start_urls[0] + b.xpath('.//h3/a/@href').extract_first().replace('../', '') """

            #2
            book_loader = ItemLoader(item=BooksItem(), selector=b)
            #3
            book_loader.default_output_processor = TakeFirst()

            #2            
            book_loader.add_xpath('title', './/h3/a/@title')
            book_loader.add_xpath('price', './/div/p[@class="price_color"]/text()')
            book_loader.add_xpath('imageurl', './/img[@class="thumbnail"]/@src')
            book_loader.add_xpath('bookurl', './/h3/a/@href')

            #3    
            print('\r\n')
            yield book_loader.load_item()

            """ with codecs.open('books.txt', 'a+', 'utf-8') as f:
                f.write(bk['title'] + '\r\n')
                f.write(bk['price'] + '\r\n')
                f.write(bk['imageurl'] + '\r\n')
                f.write(bk['bookurl'] + '\r\n\r\n') """