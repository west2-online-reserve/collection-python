# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import time

from notice import SQL
SQL = SQL.SQL


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NoticePipeline:
    def open_spider(self, spider):
        self.sql = SQL("{}{}.db".format(time.localtime().tm_mon, time.localtime().tm_mday))

    def process_item(self, item, spider):
        annex_ids = []
        for annex in item['annex']:
            self.sql['annex'].insert( [ 
                annex['title'],
                annex["url"],
                annex["download times"]
            ] )
            annex_ids.append( len(self.sql['annex']['oid']) )
        self.sql['notice'].insert([
            item['section'],
            item['title'],
            item['date'],
            item['url'],
            not not annex_ids,
            ';'.join(map(str, annex_ids))
        ])
        return item

    def close_spider(self, spider):
        del self.sql