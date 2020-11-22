#scrapy genspider --template=crawl QuoteCrawler quotes.toscrape.com
import os
import re
import codecs
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from quotes.items import QuotesItem

class QuoteCrawler(CrawlSpider):
    txt = '.txt'
    fn = 'quotes.toscrape'
    dn = fn + '.com'
    
    name = 'QuoteCrawler'
    allowed_domains = [dn]
    start_urls = ['http://' + dn + '/page/1/']

    rules = (
        #Rule(LinkExtractor(allow=r'page/'), callback='parsepage', follow=True),
        #Rule(LinkExtractor(restrict_css='span.tag-item'), callback='parsepage', follow=True),
        Rule(LinkExtractor(allow=('/tag/'), deny=('.com/page/')), callback='parsepage', follow=True),
    )
    
    def extractData(self, res):
        q = QuotesItem()

        for quote in res.css('div.quote'):
            q['quote'] = '"' + re.sub(r'[^\x00-\x7f]',r'', quote.css('span.text::text').extract_first()) + '"'
            q['author'] = quote.css('small.author::text').extract_first()
            q['tags'] = ' '.join(str(s) for s in quote.css('div.tags > a.tag::text').extract())

            self.writeTxt(q)

    def writeTxt(self, q):
        with codecs.open(self.fn + self.txt, 'a+', 'utf-8') as f:
            f.write(q['quote'] + '\r\n')
            f.write(q['author'] + '\r\n')
            f.write(q['tags'] + '\r\n\n')

    def parsepage(self, res):
        self.extractData(res)