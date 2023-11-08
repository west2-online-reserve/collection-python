import json
import scrapy
import time


class RepplySpider(scrapy.Spider):
    name = "repply"
    allowed_domains = ["api.bilibili.com"]
    start_urls = [
        "https://api.bilibili.com/x/v2/reply/wbi/main?oid=272024223&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=30744d95755c8d7792f59d7cdc249fcd&wts=1697981138"]

    def parse(self, response, *args, **kwargs):
        # 评论数据
        text_reply = json.loads(response.text)
        # 用户名uname,内容message,点赞数like,评论时间time
        list_replies = text_reply["data"]["replies"]  # 总评论列表

        for replis in list_replies:
            data_reply = {}

            data_reply.update({
                # 主评论用户名
                "uname": replis["member"]["uname"],
                # 主评论评论内容
                "message": replis["content"]["message"],
                # 主评论点赞数
                "like": replis["like"],
                # 主评论评论时间(时间戳转化格式时间)
                "time": time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(replis["ctime"])),
                # 是否为子评论
                "sub": "Not"
            })
            yield data_reply  # 返回主评论数据

            list_sub_reply = replis["replies"]  # 子评论列表

            if isinstance(list_sub_reply, list):
                for sub_reply in list_sub_reply:
                    data = {}

                    data.update({
                        # 子评论用户名
                        "uname": sub_reply["member"]["uname"],
                        # 子评论内容
                        "message": sub_reply["content"]["message"],
                        # 子评论点赞数
                        "like": sub_reply["like"],
                        # 子评论时间
                        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sub_reply["ctime"])),
                        # 是否为子评论
                        "sub": "Yes"
                    })

                    yield data  # 返回子评论数据
        print("replllllly over!!!")
