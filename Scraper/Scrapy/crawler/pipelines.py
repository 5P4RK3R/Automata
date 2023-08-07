# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item
# class PostgresPipeline:
#     def __init__(self, postgres_config):
#         self.postgres_config = postgres_config

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             postgres_config=crawler.settings.get('POSTGRES_CONFIG')
#         )

#     def open_spider(self, spider):
#         self.conn = psycopg2.connect(**self.postgres_config)
#         self.cur = self.conn.cursor()

#     def close_spider(self, spider):
#         self.cur.close()
#         self.conn.close()

#     def process_item(self, item, spider):
#         print(item,spider)
#         sql = "INSERT INTO remote (title,company,period,category,location,work_type, description,raw_description,raw_job_info) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
#         values = (item['title'],item['company'],item['period'],item['category'],item['location'],item['work_type'], item['description'],item['raw_description'],item['raw_job_info'])
#         self.cur.execute(sql, values)
#         self.conn.commit()
#         return item

import pymongo

class MyMongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(dict(item))
        return item