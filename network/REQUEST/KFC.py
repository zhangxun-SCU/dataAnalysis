import requests
import json

if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    place = input("输入关键字：")
    pageIndex = int(input("pageIndex:"))
    pageSize = int(input("pageSize:"))
    params = {
        "cname": "",
        "pid": "",
        "keyword": place,
        "pageIndex": pageIndex,
        "pageSize": pageSize,
    }
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42 '
    }
    response = requests.get(url=url, headers=headers, params=params)
    print(response.text)

