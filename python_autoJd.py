#!/usr/bin/python
# coding=utf-8
import requests
from http.cookiejar import CookieJar
from http.cookiejar import Cookie
from requests.cookies import RequestsCookieJar
import os
import re
import random
import time
cookiesText = {}
headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, compress',
    # 'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400',
}


def main():
    print("输出内容====>>>>>:", headers)
    txtPath = os.path.abspath('cookies_Jd.txt')
    cookiesTxt = open(txtPath, "r",)
    txtCookies = cookiesTxt.read()
    for lint in txtCookies.split(";"):
        name, val = lint.strip().split("=", 1)
        cookiesText[name] = val
        # id="st_788205" 正则表达式
    strurl = "https://t.jd.com/follow/vender/list.do"
    res1 = requests.request(
        method="GET",
        url=strurl,
        cookies=cookiesText,
        headers=headers
    )
    # \r\n
    content = str(res1.content.decode('utf-8'))
    backData = content
    # \r\n\t
    # .decode('utf-8')
    # backData = backData.replace("\r", "", 100000000)
    # backData = backData.replace("\n", "", 100000000)
    # backData = backData.replace("\t", "", 100000000)
    # id="st_788205"
    # print('输出内容:', str(backData))
    getId = re.findall(r'id="st_(\d+)"', backData, re.S)

    # 此处判断获取的id是否还有 有就做删除操作 没有就跳出
    if len(getId) > 0:
        deletes(getId)
    else:
        pass


def deletes(args):
    print('输出获取的关注id:', args)
    getarrStr = ','.join([str(itme) for itme in args])
    print('输出获取的数组字符串', getarrStr)
    strurl = "https://t.jd.com/follow/vender/batchUnfollow.do"
    res1 = requests.request(
        method="POST",
        url=strurl,
        cookies=cookiesText,
        headers=headers,
        data={
            "venderIds":getarrStr
        }
    )
    content = str(res1.content.decode('utf-8'))
    print('调用结果>>??',content)
    main()


# https://t.jd.com/follow/vender/batchUnfollow.do
if __name__ == "__main__":
    main()
