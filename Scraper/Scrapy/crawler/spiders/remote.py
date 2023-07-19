import scrapy
from ..items import RemoteItem
from scrapy.loader import ItemLoader

class RemoteSpider(scrapy.Spider):
    name = 'remote'
    allowed_domains = ['remote.co']
    start_urls = ['https://remote.co/remote-jobs/']

    def parse(self, response):
        # print(response.css('p.m-0'))
        self.links = response.css('div#remoteJobs a.nav-link::attr(href)').extract()
        self.logger.info(self.links)
        # url = response.urljoin(f"https://remote.co{links}")
        # self.logger.info(f"next_page {url}")
        # yield response.follow(url,callback = self.parse_jobs)
        for link in self.links:
            url = response.urljoin(f"https://remote.co{link}")
            self.logger.info(f"next_page {url}")
            yield response.follow(url,callback = self.parse_jobs)

    def parse_jobs(self, response):
        print("parse_jobs")
        self.follows = response.css('a.card::attr(href)').extract()
        self.logger.info(f"links, {self.follows}")
        # url = response.urljoin(f"https://remote.co{links}")
        # self.logger.info(f"next_page {url}")
        # yield response.follow(url,callback = self.parse_job)
        for link in self.follows:
            url = response.urljoin(f"https://remote.co{link}")
            self.logger.info(f"next_page {url}")
            yield response.follow(url,callback = self.parse_job)

    def parse_job(self, response):
        self.logger.info("parse_job")
        # data = response.css('div.job_description').get()
        il = ItemLoader(item = RemoteItem(),selector = response)
        il.add_css('title','h1.font-weight-bold')
        il.add_css('location','div.location_sm')
        il.add_css('category','div.tags_sm a::text')
        il.add_css('period','div.date_tags time::text')
        il.add_css('description','div.job_description')
        il.add_css('raw_description','div.job_description')
        il.add_css('raw_job_info','div.job_info_container_sm')
        yield il.load_item()
        # self.logger.info(data)