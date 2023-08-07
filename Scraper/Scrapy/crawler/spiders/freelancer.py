import scrapy
import time
from traceback import format_exc
# from ..item import CrawlerItem
from ..items import FreelancerItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FreelancerSpider(scrapy.Spider):
    name = 'freelancer'
    allowed_domains = ['freelancer.com']
    # allowed_domains = ['https://www.freelancer.com']
    start_urls = ['https://www.freelancer.com/jobs/']
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.links = []

    def parse(self, response):
        try:
            self.links.extend(response.css('div.JobSearchCard-item a::attr(href)').extract())
            # print(jobs)
            # self.logger.info(self.links)
            self.logger.info(len(self.links))
            # for job in response.css('div.JobSearchCard-item'):
                # il = ItemLoader(item = FreelancerItem(),selector = job)

                # il.add_css('title','a.JobSearchCard-primary-heading-link::text')
                # il.add_css('link','h2.ProjectTable-title a::attr(href)')
                # il.add_css('desc','p.JobSearchCard-primary-description::text')
                # il.add_css('skills','span.ProjectTable-skills::text')
                # il.add_css('started','td.started-col::text')
                # il.add_css('entries','td.bids-col::text')
                # il.add_css('price','div.JobSearchCard-secondary-price::text')

                # yield il.load_item()
                # price = job.css('div.JobSearchCard-secondary-price::text')
                # link = job.xpath("//h2[@class='ProjectTable-title']/a/@href")

                # title = job.css('a.JobSearchCard-primary-heading-link::text')
                # desc = job.css('p.JobSearchCard-primary-description::text')
                # skills = job.css('span.ProjectTable-skills a::attr(href)')
                # entries = job.css('div.bids-col-inner::text')
                # started = job.css('td.started-col::text')
                # yield {
                    # 'title': title.get().strip() if title else "",
                    # 'link': link.get().strip() if link else "",
                    # 'desc': desc.get().strip() if desc else "",
                    # 'price': price.get().strip() if price else "",
                    # 'skills': skills.get().strip() if skills else "",
                    # 'entries': entries.get().strip() if entries else "",
                    # 'started': started.get().strip() if started else "",
                # }

            # total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
            next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
            last_page = response.css('#bottom-pagination a:nth-last-child(1)::attr(href)').get()
            self.logger.info(next_page)
            self.logger.info(last_page)
            # next_page = int(response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get().strip('jobs/'))
            # page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
            # print("31test",next_page)
            # self.logger.info(f"31test,{total_pages},{next_page},{page}, {page is not total_pages}")
            # self.logger.info(f"total_pages {total_pages}")   
            # if next_page is not None:
            #     self.logger.info("---------------Next Page------------")
            #     self.logger.info(response)
            #     self.logger.info(f"next_page {next_page}")
            #     next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
            #     self.logger.info(f"next_page {next_page}")
            #     yield response.follow(next_page,callback = self.parse) 
            # if next_page == last_page:
            for link in self.links:
                self.logger.info(f"next_page {link}")
                next_page = response.urljoin(f"https://www.freelancer.com{link}")
                self.logger.info(f"next_page {link}")
                yield response.follow(next_page,callback = self.parse_job) 
            # if page is not total_pages:
            #     self.logger.info("---------------Next Page------------")
            #     self.logger.info(f"next_page {next_page}")
            #     next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
            #     self.logger.info(f"next_page {next_page}")
            #     yield response.follow(next_page,callback = self.parse)
                # yield scrapy.Request(next_page, callback = self.parse)
        except:
            print(format_exc())
            self.logger.error(format_exc())

    def parse_job(self, response):
        # il = ItemLoader(item = FreelancerItem(),selector = response)
        # il.add_css('title','fl-heading.Heading span::text')
        # # il.add_css('skills','fl-bit.ProjectViewDetailsSkills::text')
        # # il.add_css('raw_description','fl-bit.Card')
        # yield il.load_item()
        # skills = response.xpath('//fl-bit[@class="ProjectViewDetailsSkills"]')
        title = response.xpath('//fl-text[@class="ng-star-inserted"]')
        yield {
            # "skills": skills
            "title": title
        }

# class FreelanceSpider(CrawlSpider):
#     name = 'freelance'
#     allowed_domains = ['https://www.freelancer.com']
#     start_urls = ['https://www.freelancer.com/jobs']

#     rules = (
#         Rule(LinkExtractor(allow="jobs"),callback='parse_item'),
#     )
#     def parse_item(self, response):
#         try:
#             jobs = response.css('div.JobSearchCard-item')
#             for job in jobs:
#                 # il = itemLoader(item = CrawlerItem(),selector = job)

#                 # il.add_css('title','a.JobSearchCard-primary-heading-link::text')
#                 # il.add_css('desc','p.JobSearchCard-primary-description::text')
#                 # il.add_css('price','div.JobSearchCard-secondary-price::text')

#                 # yield il.load_item()
#                 price = job.css('div.JobSearchCard-secondary-price::text')
#                 title = job.css('a.JobSearchCard-primary-heading-link::text')
#                 desc = job.css('p.JobSearchCard-primary-description::text')
#                 yield {
#                     'title': title.get().strip() if title else "",
#                     'desc': desc.get().strip() if desc else "",
#                     'price': price.get().strip() if price else ""
#                 }

#             total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
#             next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
#             # next_page = int(response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get().strip('jobs/'))
#             page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
#             # print("31test",next_page)
#             self.logger.info(f"31test,{total_pages},{next_page},{page}, {page is not total_pages}")
#             self.logger.info(f"total_pages {total_pages}")   
#             if next_page is not None:
#                 self.logger.info("---------------Next Page------------")
#                 self.logger.info(response)
#                 self.logger.info(f"next_page {next_page}")
#                 next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
#                 self.logger.info(f"next_page {next_page}")
#                 yield response.follow(next_page,callback = self.parse)     
#             # if page is not total_pages:
#             #     self.logger.info("---------------Next Page------------")
#             #     self.logger.info(f"next_page {next_page}")
#             #     next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
#             #     self.logger.info(f"next_page {next_page}")
#             #     yield response.follow(next_page,callback = self.parse)
#                 # yield scrapy.Request(next_page, callback = self.parse)
#         except:
#             print(format_exc())

