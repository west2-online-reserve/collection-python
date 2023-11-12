import requests
import json
import time
import re


def get_Month():
    lt = time.localtime(time.time())
    lt = lt[1]
    if (lt > 9):
        return str(lt)
    else:  # 月份小于10前面加个0，保证格式
        return "0" + str(lt)


def get_Day():
    return str(time.localtime()[2])


def get_ts():  # 获取时间戳
    return time.time()


def returnApi():
    Api_list = []
    month = get_Month()
    day = get_Day()
    ts = get_ts()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    }
    url = "https://baike.baidu.com/cms/home/eventsOnHistory/" + month + ".json?_=" + str(ts)
    html = requests.get(url=url, headers=headers).json()
    for i in range(len(html[month][month + day])):  # 这个是上面url月份里具体的天数
        year = html[month][month + day][i]['year']  # 获取事件的年
        title = html[month][month + day][i]['title']  # 获取事件的标题
        link = html[month][month + day][i]['link']  # 获取事件的详情链接
        type = html[month][month + day][i]['type']  # 获取事件的类型(birthday,death,event)
        desc = html[month][month + day][i]['desc']  # 获取事件的详情
        title = re.sub(r'<.*?>', '', title)  # 去掉标题里一堆的超链接
        desc = re.sub(r'<.*?>', '', desc) + '...'  # 去掉详情里一堆的超链接
        The_Api = {"year": year, "title": title, "link": link, "desc": desc, "type": type}  # 组成一个字典
        Api_list.append(The_Api)  # 列表套字典
    return json.dumps(Api_list)  # 编码成json数据，好调用


if __name__ == '__main__':
    returnApi()
