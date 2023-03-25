import scrapy


class AngelSpider(scrapy.Spider):
    name = 'angel'
    allowed_domains = ['angel.co']
    start_urls = ['http://angel.co/']

    def parse(self, response):
        pass
