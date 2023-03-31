## Start the Scrapy Project
    scrapy startproject stack
## Create a Spider
    scrapy genspider example example.com
## Run a Spider
    scrapy runspider quotes_spider.py -o quotes.jsonl
## Write Json from scrapy
    scrapy crawl stack -o items.json -t json