import scrapy


class MusescoreSpider(scrapy.Spider):
    name = 'musescore'
    allowed_domains = ['https://musescore.com/hub/guitar']
    start_urls = ['http://https://musescore.com/hub/guitar/']

    def parse(self, response):
        pass
