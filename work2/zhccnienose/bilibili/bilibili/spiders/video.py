import requests
import scrapy
import re


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["www.bilibili.com"]
    start_urls = [
        "https://www.bilibili.com/video/BV16c41137iE/?spm_id_from=333.337.search-card.all.click&vd_source=5b0235cdfc19117d1e54ecdf10ba1755"]

    def parse(self, response, *args, **kwargs):
        data_video = {}
        text_video = response.xpath("//script[5]/text()").extract_first()
        # print(text_video)
        # 点赞数
        pat_like = r'"like":[0-9]*'
        data_video["like"] = re.findall(r'[0-9]+', re.findall(pat_like, text_video, re.MULTILINE)[0], re.S)[0]
        # 投币数
        pat_coin = r'"coin":[0-9]*'
        data_video["coin"] = re.findall(r'[0-9]+', re.findall(pat_coin, text_video, re.MULTILINE)[0], re.S)[0]
        # 收藏数
        pat_favorite = r'"favorite":[0-9]*'
        data_video["favorite"] = re.findall(r'[0-9]+', re.findall(pat_favorite, text_video, re.MULTILINE)[0], re.S)[0]
        # 评论总数
        pat_reply = r'"reply":[0-9]*'
        data_video["reply"] = re.findall(r'[0-9]+', re.findall(pat_reply, text_video, re.MULTILINE)[0], re.S)[0]

        print("demo over!!!")
        # 返回视频数据
        yield data_video
