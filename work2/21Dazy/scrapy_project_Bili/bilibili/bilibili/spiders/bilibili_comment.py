from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response
import re
from bilibili.items import BilibiliItem,videoItem
import datetime
import time
import hashlib
pattern_reply_member=r'https://api.bilibili.com/x/v2/reply/wbi/main.*?'
pattern_base_data=r'https://www.bilibili.com/video/.*?'
#pattern_pagination_str=r'.*?(mode=3&)'
xpath_likes='/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/span//text()'#点赞数xpath
xpath_coins='/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div/span//text()'#硬币数量
xpath_fav='/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]/div/span//text()'#收藏数量
xpath_comments='/html/body/div[2]/div[2]/div[1]/div[4]/div[3]/div/div/div/div[1]/div/ul/li[1]/span[2]//text()'#评论数量
ct="ea1db124af3c7062474693fa704f4ff8"#md5加密的密钥


def parse_reply(item,reply):
        member=reply['member']#这里的member仍然是一个字典，我们需要基础的收集mid，和uname两个键值对
        reply_content=reply['content']#content是一个字典，其中message存放评论的内容（也包括空白字符）
        mid=member['mid']#评论人的数字id
        uname=member['uname']#用户的名字
        likes=reply['like']#评论点赞数
        time_base=reply['ctime']
        message_base=reply_content['message']#包含空白字符的评论内容
        message_changed=re.sub(r'\[\S+\]',' ',message_base)#去除了表情符号
        item['mid']=mid
        item['uname']=uname
        item['content']=message_changed
        item['com_likes']=likes
        item['time']=datetime.datetime.fromtimestamp(time_base).strftime('%Y-%m-%d %H:%M:%S')
       
        
class BilibiliCommentSpider(scrapy.Spider):
    date_time=str(int(time.time()))#当前时间戳
    base_rurl="https://api.bilibili.com/x/v2/reply/wbi/main?oid=577899221&type=1&mode=3&pagination_str={}&plat=1&seek_rpid=&web_location=1315875&w_rid={}&wts={}"
    pagination_str=""#会发生变化的参数
    print(date_time)
    videoitem=videoItem()
    com_num=0#用来统计已经获取的评论个数
    comment_num=0#评论总数
    name = "bilibili_comment"
    flag=1
   # allowed_domains = ["https://www.bilibili.com/video/BV1Yh411o7Sz"]
    start_urls = ["https://www.bilibili.com/video/BV1Sa4y1D7bR","https://api.bilibili.com/x/v2/reply/wbi/main?oid=663059358&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=e5b0c4eb22452e468bfd29ab2b86dacd&wts=1699237424"]#一个是视频页url，一个是评论内容url
    # def get_oid(bv_id):#将视频的bv号转化为oid
    # base_url="https://www.bilibili.com/video/"
    # bv_url=base_url+bv_id
    oid=None
    son_reply_url_BASE='https://api.bilibili.com/x/v2/reply/reply?oid={}&type=1&root={}&ps=10&pn={}&web_location:333.788'#用于迭代子评论url
    def start_requests(self):
        for url in self.start_urls:
            if re.match(pattern_reply_member,url):
                
                yield scrapy.Request(url=url,callback=self.parse_reply_member)
            if re.match(pattern_base_data,url):
                
                yield scrapy.Request(url=url,callback=self.parse_base_data)
            else:
                return "网址输入错误"
           
    def parse_base_data(self,response):
        likes=response.xpath(xpath_likes)[0].extract()
        coins=response.xpath(xpath_coins)[0].extract()
        fav_nums=response.xpath(xpath_fav)[0].extract()
        self.videoitem['likes']=likes
        self.videoitem['coins']=coins
        self.videoitem['fav']=fav_nums
        print('点赞数',likes,'硬币数',coins,'收藏数',fav_nums,'评论数',self.videoitem['comments'])
        
    def parse_son_reply(self, response):
        son_replies = response.json()
        items_son_replies = BilibiliItem()
        sreply_num = son_replies['data']['page']['count']  # 子评论总数
        self.com_num+=sreply_num
        page_max = (sreply_num +10-1)// 10
        pn = response.meta['pn']  # 子评论页数
        oid = response.meta['oid']  # 视频id
        root_id = response.meta['root_id']  # 根评论id
        if son_replies['data']['replies'] is not None:
            for i in range(len(son_replies['data']['replies'])):
                items_son_replies = BilibiliItem()
                parse_reply(items_son_replies, son_replies['data']['replies'][i])
                yield items_son_replies
            if page_max > pn:
                pn += 1
                new_son_url = self.son_reply_url_BASE.format(oid, root_id, pn)
                yield scrapy.Request(url=new_son_url, callback=self.parse_son_reply, meta={'pn': pn, 'oid': oid, 'root_id': root_id})
  
    def parse_reply_member(self, response):  
        replies=response.json()
        if self.flag:
            self.comment_num=replies['data']['cursor']['all_count']#评论数量
            self.videoitem['comments']=self.comment_num
            self.flag=0
       # print(' 评论数',comment_num)
        items_top=BilibiliItem()#先判断是否存在置顶评论
        if replies['data']['top_replies'] is not None:
            self.com_num+=1
            parse_reply(items_top,replies['data']['top_replies'][0])
            yield items_top
        self.com_num+=len(replies['data']['replies'])
        for i in range(len(replies['data']['replies'])):#每一个reply是一个根评论的字典，我们只需要这个字典里member和replies两个键值对就行
            items_test=BilibiliItem()
            parse_reply(items_test,replies['data']['replies'][i])
            
            
            yield items_test
            if replies['data']['replies'][i]['replies'] is not None:#如果存在子评论，则生成子评论ajax请求，并回调至parse_son_reply
                root_id=replies['data']['replies'][i]['replies'][0]['rpid']
                oid=replies['data']['replies'][i]['replies'][0]['oid']
                pn=1
                son_reply_url=self.son_reply_url_BASE.format(oid,root_id,pn)
                
                yield scrapy.Request(url=son_reply_url,callback=self.parse_son_reply,meta={'oid':oid,'root_id':root_id,'pn':pn})
        if self.com_num<self.comment_num:
            self.date_time=time.time()
            yield scrapy.Request(url=self.start_urls[1],callback=self.parse_reply_member,dont_filter=True)
            print('下一页')
        else:
            print('爬取完成')  
            