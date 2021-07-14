# -*- coding: utf-8 -*-
# python 3

# 抓取 ptt 八卦版的網頁原始碼(HTML)
# mac 需先引用ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
def getData(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')
        
    # print(data)

    # 解析原始碼，取得每篇文章的標題
    import bs4 
    root = bs4.BeautifulSoup(data, "html.parser") # 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 beautifulsoup4，他會幫我們用 html 解析。
    # print(root.title.string)
    titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
    # print(titles)
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤（沒有被刪除），印出來
            print(title.a.string)
    # 抓取下一頁連結
    nextLink=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]
# 主程序，抓取多個頁面的標題
pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1
# pageUrl="https://www.ptt.cc"+getData(pageUrl)
# print(pageUrl)
