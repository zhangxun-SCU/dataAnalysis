import requests
# sogou首页数据


if __name__ == '__main__':
    # 指定url
    url = "https://www.sogou.com/"
    # 发起请求,get方法返回一个响应对象
    response = requests.get(url=url)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open("data/sogou.html", 'w', encoding="utf-8") as f:
        f.write(page_text)
