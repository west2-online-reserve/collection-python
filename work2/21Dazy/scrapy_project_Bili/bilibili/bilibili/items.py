# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    mid=scrapy.Field()#评论人数字id
    uname=scrapy.Field()#评论人姓名
    content=scrapy.Field()#评论内容
    com_likes=scrapy.Field()#评论点赞数量
    time=scrapy.Field()#评论时间
class videoItem(scrapy.Item):
    likes=scrapy.Field()
    comments=scrapy.Field()
    fav=scrapy.Field()
    coins=scrapy.Field()