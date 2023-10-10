# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date    = scrapy.Field()
    section = scrapy.Field()
    title   = scrapy.Field()
    post_time = scrapy.Field()
    brief   = scrapy.Field()

    content = scrapy.Field()

    url     = scrapy.Field()

    annex   = scrapy.Field()
