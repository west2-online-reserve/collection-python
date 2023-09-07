import json
import os
import re

import time
import requests

from SQL import SQL

url = 'https://baike.baidu.com/cms/home/eventsOnHistory/{}.json'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'baike.baidu.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

'''
response = requests.get(url=url.format("%02d"%mon), headers=headers)
with open("data/%02d"%mon + '.json','w+',encoding=response.encoding) as fout:
    json.dump(response.json(), fout)
print("%02d"%mon + ' is ended')
time.sleep(3)
'''

db = SQL("today_in_history.db")

no_tag = re.compile(r'<[\s\S]+?>|\[[\s\S]+?\]')
no_space = re.compile(r'\s|"')
no = lambda s:no_space.sub('', no_tag.sub('', s) )

for mon in range(1,13):
    if(os.path.exists("data")):
        with open("data/%02d.json"%mon) as fin:
            monthly = json.load(fin)
    else:
        response = requests.get(url=url.format("%02d"%mon), headers=headers)
        monthly  = response.json()
    monthly = monthly[ "%02d"%mon ]

    for index in monthly.keys():
        daily = monthly[index]
        db[index] = ['year', 'type', 'title', 'content']
        for item in daily:
            try:
                db[index]['text'] = [ no(item['year']),  no(item['type']), no(item['title']), no(item['desc'])]
            except Exception as e:
                print('------')
                print(e)
                print(item)
                print([ no(item['year']),  no(item['type']), no(item['title']), no(item['desc'])])
                print('======')

del db