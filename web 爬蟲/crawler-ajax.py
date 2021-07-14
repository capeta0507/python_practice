# -*- coding: utf-8 -*-
# python 3

# 抓取 kkday 的文章資料
# mac 需先引用ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
# import urllib
# https://www.kkday.com/zh-tw
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=a02948a0c6fbb3c4c52aa2d08104f49c"
# 建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode('utf-8') # 根據觀察，取得的資料是 JSON 格式
    
# print(data)

# 解析 JSON 格式的資料，取得每篇文章的標題
import json 
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# print(data)
# 取得 JSON 資料中的文章標題
posts=data["data"]["homepage_product_group"]
# print(posts)
for post in posts:
    # post=posts[key]
    print(post["title"])