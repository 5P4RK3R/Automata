# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


def stripText(text):
    return text.strip()
def joinText(text):
    return text.join()

class FreelancerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    link = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    desc = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # skills = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = Join())
    # started = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # entries = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # pass

class RemoteItem(scrapy.Item):
    location = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    title = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    period = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    category = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    description = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    raw_description = scrapy.Field(input_processor = MapCompose(stripText),output_processor = TakeFirst())
    raw_job_info = scrapy.Field(input_processor = MapCompose(stripText),output_processor = TakeFirst())
