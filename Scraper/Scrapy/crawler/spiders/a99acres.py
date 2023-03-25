import scrapy
# from stack.items import StackItem


class A99acresSpider(scrapy.Spider):
    name = '99acres'
    allowed_domains = ['https://www.99acres.com/independent-house-for-rent-in-india-ffid']
    start_urls = ['http://https://www.99acres.com/independent-house-for-rent-in-india-ffid/']

    def parse(self, response):
        lands = response.css('div.pageComponent')
        for land in lands:
            # item = StackItem()
            yield {
                "price": land.css("#srp_tuple_price::text").get().strip()
            }
