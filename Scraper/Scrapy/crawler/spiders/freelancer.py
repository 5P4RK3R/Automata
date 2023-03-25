import scrapy
import time
# from ..item import CrawlerItem
# from scrapy.loader import itemLoader

class FreelancerSpider(scrapy.Spider):
    name = 'freelancer'
    allowed_domains = ['https://www.freelancer.com/jobs']
    start_urls = ['https://www.freelancer.com/jobs']

    def parse(self, response):
        jobs = response.css('div.JobSearchCard-item')
        for job in jobs:
            # il = itemLoader(item = CrawlerItem(),selector = job)

            # il.add_css('title','a.JobSearchCard-primary-heading-link::text')
            # il.add_css('desc','p.JobSearchCard-primary-description::text')
            # il.add_css('price','div.JobSearchCard-secondary-price::text')

            # yield il.load_item()

            yield {
                'title': job.css('a.JobSearchCard-primary-heading-link::text').get().strip(),
                'desc': job.css('p.JobSearchCard-primary-description::text').get().strip(),
                'price':job.css('div.JobSearchCard-secondary-price::text').get().strip()
            }

        total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
        next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
        page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
        print(total_pages,next_page,page, page is not total_pages)
        
        if page is not total_pages:
            print("---------------Next Page------------")
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback = self.parse)

