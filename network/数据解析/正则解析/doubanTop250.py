import requests
import re
import csv

if __name__ == "__main__":
    for i in range(0, 251, 25):
        print(i)
        url = f"https://movie.douban.com/top250?start={i}&filter="

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42 '
        }
        Top250 = requests.get(url=url, headers=headers).text

        # 正则解析: 先查看页面源代码去定位
        re_obj = re.compile(
            r'<li>.*?<div class="item">.*?<span class="title">(?P<movieName>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<scores>.*?)</span>',
            re.S)
        result = re_obj.finditer(Top250)

        with open("data/doubanTop250.csv", 'a', encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            for it in result:
                dic = it.groupdict()
                csvwriter.writerow(dic.values())

