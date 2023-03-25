import scrapy
# from stack.items import StackItem
from scrapy.selector import Selector


class A99acresSpider(scrapy.Spider):
    name = '99acres'
    allowed_domains = ['https://www.99acres.com/independent-house-for-rent-in-india-ffid']
    start_urls = ['http://https://www.99acres.com/independent-house-for-rent-in-india-ffid/']

    def parse(self, response):
        lands = Selector(response).xpath('//div[@data-label="SEARCH"]')
        # lands = response.css('div.pageComponent')
        print("lands",lands)
        for land in lands:
            # item = StackItem()
            yield {
                "price": land.css("#srp_tuple_price::text").get().strip()
            }
