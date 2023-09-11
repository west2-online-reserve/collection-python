import re
import requests
import scrapy
import time


from ..items import NoticeItem
from ..SQL   import SQL

got = 0
want  = 100

is_create_information = False


def get_times(script):
    url = "https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp"
    ans = re.split(r'[(,")]',script)
    params = {
        "wbnewsid":ans[1],
        "owner":ans[2],
        "type":"wbnewsfile",
        "randomid":"nattach"
    }
    return requests.get(url, params=params).json()['wbshowtimes']



class NoticeSpider(scrapy.Spider):
    name = "notice"
    allowed_domains = ["jwch.fzu.edu.cn"]

    def start_requests(self):
        db = SQL("{}{}.db".format(time.localtime().tm_mon, time.localtime().tm_mday))
        db["notice"].create(["station", "title", "date", "url", "is having annex", "oid of annex"])
        db["annex"] .create(["name", "url", "download times"])
        del db

        home = 'https://jwch.fzu.edu.cn/jxtz.htm'
        yield scrapy.Request(home, callback=self.parse_list)

    
    def parse_list(self, response):
        global got,is_create_information

        db = SQL("{}{}.db".format(time.localtime().tm_mon, time.localtime().tm_mday))
        if(not is_create_information):
            db['information'].create(['save time', 'totol pages'])
            db['information'].insert([
                time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),
                response.xpath('//span[@class="p_no"]')[-1].xpath('./a/text()').get()
            ])
            is_create_information = True
        del db

        notice_list = response.xpath('//ul[@class="list-gl"]/li')
        for span in notice_list:
            got += 1
            self.log(f"loading url === {span.xpath('./a/@href').get()}")
            if( got>want ):
                self.log("end loading url ===")
                break
            yield response.follow(span.xpath('./a')[0], callback=self.parse_notice)
        else:
            next = response.xpath("//span[@class='p_next p_fun']/a")[0]
            self.log(f'loading next menu === {next.get()}')
            yield response.follow(next, callback=self.parse_list)


    def parse_notice(self, response):
        filename= response.url.split('/')[-1]
        try:
            pass
            #with open(filename, 'wb') as fout:
        #        fout.write(response.body)
        except:
            self.log( f"{filename} hava an error in saving process" )
        self.log("第{}/{}页爬取完毕".format(got-1, want))

        result = NoticeItem()

        try:
            result['section']   = response.xpath('//p[@class="w-main-dh-text"]/a')[-1].xpath('./text()').extract_first()
            result['title']     = response.xpath('//h4[@align="center"]/text()').extract_first()
            result['post_time'] = response.xpath('//span[@class="xl_sj_icon"]/text()')[0].re(r"\d{4}-\d{2}-\d{2}")[0]
            result['brief']     = response.xpath('//meta[@name="description"]/@content').extract_first()
            result['date']      = response.xpath('.').re('\d{4}-\d{2}-\d{2}')[0]
            result['url']       = response.url
        except Exception as e:
            self.log("解析 {} 的基础数据失败".format(filename))
            self.log("发生了 {} 错误".format(e))

        try:
            result['content'] = '\n'.join( [ item.xpath('string(.)').get() for item in response.xpath('//div[@class="v_news_content"]/p') ] )
        except Exception as e:
            self.log("解析 {} 的内容失败".format(filename))
            self.log("发生了 {} 错误".format(e))

        try:
            annex = response.xpath('//ul[@style="list-style-type:none;"]/li')
            result['annex'] = []
            for item in annex:
                result['annex'].append({
                    "title":item.xpath('./a/text()').get(),
                    "url"  :item.xpath('./a/@href').get(),
                    "download times": get_times( item.xpath('./span/script/text()').get() )
                })
        except Exception as e:
            self.log("解析 {} 的附件失败".format(filename))
            self.log("发生了 {} 错误".format(e))


        yield result