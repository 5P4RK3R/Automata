# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def stripText(text):
    return text.strip()

class FreelancerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    desc = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # pass
