# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#爬虫获取到的数据需要组装成item对象
class jiaowuItem(scrapy.Item):
    time = scrapy.Field()
    tzr = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    annex_title = scrapy.Field()
    annex_link = scrapy.Field()
    annex_download_times = scrapy.Field()


