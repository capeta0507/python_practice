# -*- coding: utf-8 -*-
# 網路連線
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得台灣大學網站的原始碼（HTML、CSS、JS）
# print(data)
# 串接、擷取公開資料
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 模組處理 json 資料格式
# print(data)
# 取得公司名稱
clist=data["result"]["results"]
# print(clist)
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")