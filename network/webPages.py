"""
user-agent(请求载体身份标识)
UA检测：门户网站的服务器会检测对应请求的身份标识，如果检测到请求的载体身份标识为
某一款浏览器，就说明请求是正常的请求，由用户发起；但如果检测到身份标识不是某一款浏览器的
就表示请求是一个不正常的请求，由爬虫发起，服务器可能会拒绝请求。
UA伪装：所以爬虫一定要进行UA伪装，让爬虫对应的请求载体身份标识伪装成一款浏览器
"""
import requests


if __name__ == '__main__':
    # UA伪装，将对应的UA封装进字典
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42 '
    }
    url = "https://www.sogou.com/web"
    # 处理url携带参数, 封装进字典
    key = input("输入关键词：")
    param = {
        'query': key,
    }
    # params可直接接收我们的参数字典, headers是发起请求的头信息
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    with open(f"data/{key}.html", 'w', encoding="utf-8") as f:
        f.write(page_text)
        print("保存成功")
