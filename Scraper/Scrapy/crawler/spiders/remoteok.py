import scrapy


class RemoteokSpider(scrapy.Spider):
    name = 'remoteok'
    allowed_domains = ['https://remoteok.com/']
    start_urls = ['https://remoteok.com/']

    def parse(self, response):
        jobs = response.css('li.feature')
        for job in jobs:
            yield{
                'company': job.css('span.company::text').get(),
                'title': job.css('span.title::text').get(),
                'region': job.css('span.region::text').get()
            }
