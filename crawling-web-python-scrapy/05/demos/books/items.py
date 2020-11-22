#2 - input processors and item loaders
import scrapy
from scrapy.loader.processors import MapCompose #2

#2
def addlink(url):
    return'http://books.toscrape.com/' + url.replace('../', '')

class BooksItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    """ imageurl = scrapy.Field()
    bookurl = scrapy.Field() """
    #2
    imageurl = scrapy.Field(input_processor = MapCompose(addlink))
    bookurl = scrapy.Field(input_processor = MapCompose(addlink))
