import scrapy


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['https://www.magnatiles.com/']
    start_urls = ['https://www.magnatiles.com/']

    def parse(self, response):
        tiles = response.css('li.product')
        for tile in tiles:
            yield{
                'name': tile.css('h2.woocommerce-loop-product__title::text').get(),
                'price': tile.css('span.woocommerce-Price-currencySymbol::text').get() + tile.css('bdi::text').get() 
            }
