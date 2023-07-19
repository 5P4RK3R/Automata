import scrapy


class WeworkremotelySpider(scrapy.Spider):
    name = 'weworkremotely'
    allowed_domains = ['weworkremotely.com']
    start_urls = ['https://weworkremotely.com/']

    def parse(self, response):
        self.links = response.css('section.jobs li.view-all a::attr(href)').extract()
        self.follows = response.css('section.jobs ul li a::attr(href)').extract()
        self.logger.info(f"links {self.links}")
        self.logger.info(f"follows {self.follows}")
        self.logger.info(f"length {len(self.follows)}")
        for link in self.links:
            url = response.urljoin(f"https://weworkremotely.com{link}")
            self.logger.info(f"next_page {url}")
            yield response.follow(url,callback = self.parse_jobs)

    def parse_jobs(self, response):
        self.follows.extend(response.css('section.jobs ul li a::attr(href)').extract())
        self.logger.info(f"follows {self.follows}")
        self.logger.info(f"len {len(self.follows)}")
        for follow in self.follows:
            url = response.urljoin(f"https://weworkremotely.com{follow}")
            self.logger.info(f"next_page {url}")
            yield response.follow(url,callback = self.parse_job)

    def parse_job(self, response):
        pass