import json
import re
import requests
import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from west2.items import fzuItem


class FzuSpider(scrapy.Spider):
    name = "fzu"
    allowed_domains = ["jwch.fzu.edu.cn"]
    start_urls = ["https://jwch.fzu.edu.cn/jxtz.htm"]

    def get_count(self, s):
        url2 = "https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp"
        ans = re.split(r'[(,")]', s)
        params = {
            'wbnewsid': ans[1],
            'owner': ans[2],
            'type': 'wbnewsfile',
            'randomid': 'nattach'
        }
        response = requests.get(url=url2, params=params)
        if response.status_code == 200 and response.text:
            try:
                json_data = response.json()
                # 然后从json_data中提取所需的信息
                return json_data['wbshowtimes']
            except json.decoder.JSONDecodeError as e:
                return 0

        # 处理JSON解析错误
        else:
            # 处理响应为空或状态码不为200的情况
            pass

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        total_page = sel.css("body > div.page > div.w-main > div.wapper > div > div > div:nth-child(3) > div.ecms_pag "
                             "> div.ecms_pagination > div > span.p_pages > span:nth-child(9) > a::text").extract_first()
        print(total_page)
        items_list = sel.css("body > div.page > div.w-main > div.wapper > div > div > div:nth-child(3) > "
                             "div.box-gl.clearfix > ul > li")

        for item in items_list:
            fzu_item = fzuItem()
            fzu_item['date'] = item.css("span.doclist_time::text").extract_first().strip()
            fzu_item['type'] = item.xpath("./text()")[1].get().strip()
            fzu_item['title'] = item.css("a::attr(title)").extract_first()
            detail_url = response.urljoin(item.css("a::attr(href)").extract_first())
            fzu_item['link'] = detail_url
            yield Request(url=detail_url, callback=self.parse_details, cb_kwargs={'item': fzu_item})

        # 不知道出了什么问题但就是有问题的一行代码
        # hrefs_list = sel.css(".p_no a::attr(href)").extract()

        links = sel.xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/div[1]/div/span[1]")  # 定位
        my_links = []
        for link in links:
            href_values = link.xpath(".//a/@href")  # 匹配，生成String列表
            for href in href_values:
                full = "https://jwch.fzu.edu.cn/" + href.get()
                my_links.append(full)  # 将所有link存入myLinks
            my_links = my_links[0:4]  # 截取前四个
        for link in my_links:
            yield Request(url=link)

    def parse_details(self, response: HtmlResponse, **kwargs):
        fzu_item = kwargs['item']
        sel = Selector(response)
        details = sel.xpath('/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li')
        fzu_item['file_name'] = details.xpath(".//a/text()").extract()

        url_list = details.xpath(".//a/@href").extract()
        # 初始化一个字典，用于存储URL和拼接后的结果
        url_response_map = {}
        # 遍历URL列表并执行拼接
        mark = 1
        for url in url_list:
            # 使用urljoin将URL与response.url拼接
            full_url = response.urljoin(url)
            # 将拼接后的URL存储在字典中，以URL为键，拼接后的结果为值
            url_response_map['附件'+str(mark)] = full_url
            mark += 1
        # 将url_response_map存储到fzuItem对象的file_link字段中
        fzu_item['file_link'] = url_response_map

        count_list = details.xpath(".//span/script/text()").extract()
        count_map = []
        for count in count_list:
            count_get = self.get_count(count)
            count_map.append(count_get)
        fzu_item['file_count'] = count_map

        yield fzu_item
