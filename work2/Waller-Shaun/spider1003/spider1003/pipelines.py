# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
import pymysql

class Spider1003Pipeline:
    def __init__(self):
        self.conn = pymysql.connect(host = 'localhost',port=3306,user='root',password ='040426',database = 'spider',charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self,spider):
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title','')
        creator = item.get('tzr','')
        link = item.get('link','')
        time = item.get('time','')

        annex_title = item.get('annex_title','')
        annex_link = item.get('annex_link','')
        annex_download_times = item.get('annex_download_times','')

        self.data.append((title,creator,link,time,
                          annex_title,annex_link,annex_download_times,
                          ))
        self._write_to_db()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into FZU_edu_jxtz (`title`,`creator`,`link`,`time`,`annex_title`,`annex_link`,`annex_download_times`) values(%s,%s,%s,%s,%s,%s,%s)',self.data
        )
        self.conn.commit()
        self.data.clear()