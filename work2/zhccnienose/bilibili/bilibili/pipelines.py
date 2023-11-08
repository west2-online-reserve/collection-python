# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class BilibiliPipelineVideo:

    def open_spider(self, spider):
        if spider.name == "demo":
            self.db = pymysql.connect(host="localhost",
                                      user="root",
                                      password="C310257813.",
                                      database="video")
            self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        if spider.name == "demo":
            ins_video = "INSERT INTO `data_video` (`FAVORITE`,`REPLY`,`COIN`,`LIKE`) VALUES(%s, %s, %s, %s)"
            self.cursor.execute(ins_video,(item["favorite"], item["reply"], item["coin"], item["like"]))
            self.db.commit()

        return item

    def close_spider(self, spider):
        if spider.name == "demo":
            self.db.close()


class BilibiliPipelineReply:

    def open_spider(self, spider):
        if spider.name == "repply":
            self.db = pymysql.connect(host="localhost",
                                      user="root",
                                      password="C310257813.",
                                      database="video")
            self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        if spider.name == "repply":
            ins_reply = "INSERT INTO `DATA_REPLY` (`UNAME`,`MESSAGE`,`LIKE`,`TIME`,`SUB`) VALUES(%s, %s, %s, %s, %s)"
            self.cursor.execute(ins_reply, (item["uname"], item["message"], item["like"], item["time"], item["sub"]))
            self.db.commit()

        return item

    def close_spider(self, spider):
        if spider.name == "repply":
            self.db.close()
