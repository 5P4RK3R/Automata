import scrapy
import time
from traceback import format_exc
# from ..item import CrawlerItem
# from scrapy.loader import itemLoader

class FreelancerSpider(scrapy.Spider):
    name = 'freelancer'
    allowed_domains = ['https://www.freelancer.com/jobs']
    start_urls = ['https://www.freelancer.com/jobs']

    def parse(self, response):
        try:
            jobs = response.css('div.JobSearchCard-item')
            for job in jobs:
                # il = itemLoader(item = CrawlerItem(),selector = job)

                # il.add_css('title','a.JobSearchCard-primary-heading-link::text')
                # il.add_css('desc','p.JobSearchCard-primary-description::text')
                # il.add_css('price','div.JobSearchCard-secondary-price::text')

                # yield il.load_item()
                price = job.css('div.JobSearchCard-secondary-price::text')
                title = job.css('a.JobSearchCard-primary-heading-link::text')
                desc = job.css('p.JobSearchCard-primary-description::text')
                yield {
                    'title': title.get().strip() if title else "",
                    'desc': desc.get().strip() if desc else "",
                    'price': price.get().strip() if price else ""
                }

            total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
            next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
            # next_page = int(response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get().strip('jobs/'))
            page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
            # print("31test",next_page)
            self.logger.info(f"31test,{total_pages},{next_page},{page}, {page is not total_pages}")
            self.logger.info(f"total_pages {total_pages}")        
            if page is not total_pages:
                self.logger.info("---------------Next Page------------")
                self.logger.info(f"next_page {next_page}")
                next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
                self.logger.info(f"next_page {next_page}")
                # yield response.follow(next_page,self.parse)
                yield scrapy.Request(next_page, callback = self.parse)
        except:
            print(format_exc())

