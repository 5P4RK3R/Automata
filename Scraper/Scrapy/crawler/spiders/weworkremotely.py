import scrapy


class WeworkremotelySpider(scrapy.Spider):
    name = 'weworkremotely'
    allowed_domains = ['weworkremotely.com']
    start_urls = ['https://weworkremotely.com/']

    def parse(self, response):
        self.links = response.css('section.jobs li.view-all a::attr(href)').extract()
        self.follows = response.css('section.jobs ul li a::attr(href)').extract()
        self.logger.info(f"links {self.links}")
        self.logger.info(f"links {self.follows}")
