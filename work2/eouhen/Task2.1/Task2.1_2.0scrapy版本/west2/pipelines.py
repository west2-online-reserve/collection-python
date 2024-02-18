# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pymysql


class DbPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='0623Hathaway',
                                    database='west2', charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        type = item.get('type', '')
        date = item.get('date', '')
        link = item.get('link', '')
        title = item.get('title', '')
        file_name = '\n'.join(item.get('file_name', ''))
        file_count = '\n'.join(str(count) for count in item.get('file_count', []))
        # file_link = '\n'.join(item.get('file_link', ''))
        file_link = '\n'.join(item.get('file_link', {}).values())
        self.cursor.execute(
            'INSERT INTO fzu (type, date, link, title, file_name, file_count, file_link) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (type, date, link, title, file_name, file_count, file_link)
        )
        return item
