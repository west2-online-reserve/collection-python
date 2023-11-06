# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class fzuItem(scrapy.Item):
    type = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    file_name = scrapy.Field()
    file_link = scrapy.Field()
    file_count = scrapy.Field()
