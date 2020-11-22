# -*- coding: utf-8 -*-
import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'BookSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
