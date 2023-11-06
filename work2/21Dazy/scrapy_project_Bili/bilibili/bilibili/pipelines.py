# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


    
    
class BilibiliPipeline_root(object):
    fp=None
    
    def open_spider(self,spider):
        print("管道一开始存储")
        self.fp=open("./bilibili_test.txt",'w+',encoding='utf_8')
    def process_item(self, item, spider):
       
        mid=item['mid'].encode('utf-8').decode('utf-8')
        uname=item['uname'].encode('utf-8').decode('utf-8')
        content=item['content'].encode('utf-8').decode('utf-8')
        likes=str(item['com_likes'])
        time=item['time'].encode('utf-8').decode('utf-8')
    
        self.fp.write(mid+'  ---  '+uname+'\n'+content+'\n'+'点赞数：'+likes+"\n发布时间:"+time)
        self.fp.write("\n---------------------------------------------------------\n")    
        return item
       
    def close_spider(self,spider):
        self.fp.close()
        print("管道一结束存储")

class SQLbilibiliPipeline(object):
    db=None
    cur=None
    create_table='create table B_comments(mid text,uname text,content text,com_likes int,time text)'
    drop_table='drop table B_comments'
    def open_spider(self,spider):
        print("管道二开始存储")
        self.db=pymysql.connect(host="localhost",user="root",password="yby258014",db="bilibili",charset="utf8mb4",collation="utf8mb4_general_ci")
        self.cur=self.db.cursor()
        try:
            self.cur.execute(self.create_table)
        except:
            print("表已存在")
            self.cur.execute(self.drop_table)
            self.cur.execute(self.create_table)
            print("更新表单")
            
        else:
            print("创建最新表单")
    def process_item(self, item, spider):
        mid=item['mid'].encode('utf-8').decode('utf-8')
        uname=item['uname'].encode('utf-8').decode('utf-8')
        content=item['content'].encode('utf-8').decode('utf-8')
        likes=item['com_likes']
        time=item['time'].encode('utf-8').decode('utf-8')
        self.cur.execute("insert into B_comments(mid,uname,content,com_likes,time) values(%s,%s,%s,%s,%s)",(mid,uname,content,likes,time))
        self.db.commit()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.db.close()
        print("管道二结束存储")