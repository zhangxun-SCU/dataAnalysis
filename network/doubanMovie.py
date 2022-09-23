"""

"""
import requests
import json

if __name__ == '__main__':
    # url
    url = 'https://movie.douban.com/j/chart/top_list?'
    start = input("从第几部开始(第一部是0)")
    limit = input("爬取多少部")
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': start,  # 从库中第几部电影开始取
        'limit': limit,  # 一次取出的个数
    }
    # UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42 '
    }
    response = requests.get(url=url, headers=headers, params=params)
    response_list = response.json()
    with open('data/movie/doubanMovie.json', 'w', encoding='utf-8') as f:
        json.dump(response_list, fp=f, ensure_ascii=False)
        print("over")
