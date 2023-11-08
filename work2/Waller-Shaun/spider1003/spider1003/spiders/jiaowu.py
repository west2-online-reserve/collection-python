import re

import requests
import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from spider1003.items import jiaowuItem


def get_times(script):
    #获取点击次数
    url = r'https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp'
    ans = re.split(r'[(,")]',script)
    params = {
        'wbnewsid': ans[1],
        'owner': ans[2],
        'type': 'wbnewsfile',
        'randomid': 'nattach',
    }
    return requests.get(url=url,params=params).json()['wbshowtimes']

class JiaowuSpider(scrapy.Spider):
    name = "jiaowu"
    allowed_domains = ["jwch.fzu.edu.cn"]
    start_urls = ["https://jwch.fzu.edu.cn/jxtz.htm"]

    def parse(self, response: HtmlResponse,**kwargs):#解析页面的代码写在这里
        #拿到相应后包装成selector对象
        sel = Selector(response)
        pages = 20  #自定义爬取页数
        list_items = sel.css('body > div.page > div.w-main > div.wapper > div > div > div:nth-child(3) > div.box-gl.clearfix > ul > li')#拿到列表项
        for list_item in list_items:
            jiaowu_item = jiaowuItem()
            try:
                TAT = list_item.css('span.doclist_time::text')
                jiaowu_item['time'] = int(''.join(re.findall(r"\d+\.?\d*", TAT.extract_first())))
            except:
                TAT = list_item.css('span > font ::text')
                jiaowu_item['time'] = int(''.join(re.findall(r"\d+\.?\d*", TAT.extract_first())))
            tzr_before = list_item.xpath('span[@class="doclist_time"]/following-sibling::text()').get().strip()
            jiaowu_item['tzr'] = tzr_before
            jiaowu_item['title'] = list_item.css('a::text').extract_first()
            link =  response.urljoin(list_item.css('a::attr(href)').extract_first())
            jiaowu_item['link'] = link
            yield Request(url=link,callback=self.new_parse_detail,
                          cb_kwargs={'item':jiaowu_item})

        page_links = sel.css('div.ecms_pag > div.ecms_pagination > div > span.p_pages > span.p_no')
        whole_page_num = page_links[-1].css('a::text').extract_first()
        for i in range(2,pages+1):
            n = int(whole_page_num) - int(i)
            yield Request(url="https://jwch.fzu.edu.cn/jxtz/{}.htm".format(n))

    def new_parse_detail(self,response:HtmlResponse,**kwargs):
        jiaowu_item = kwargs['item']
        sel = Selector(response)
        links,titles,times = [],[],[]
        try:
            list_items = sel.css('body > div.page > div.w-main > div.wapper > form > div > div.ny_box > div > ul > li')
            for list_item in list_items:
                link = response.urljoin(list_item.css('a::attr(href)').extract_first())
                title = list_item.css('a::text').extract_first()
                time = str(get_times(list_item.xpath('./span/script/text()').get()))
                links.append(link)
                titles.append(title)
                times.append(time)
            jiaowu_item['annex_title'] = ';'.join(titles)
            jiaowu_item['annex_link'] = ';'.join(links)
            jiaowu_item['annex_download_times'] = ';'.join(times)
            yield jiaowu_item
        except Exception as e:
            yield jiaowu_item