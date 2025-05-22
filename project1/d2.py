# 使用requests库爬取百度网页的html数据
import requests
from fake_useragent import FakeUserAgent

url = 'https://www.baidu.com'

# 定义用户代理
headers = {'User-Agent': FakeUserAgent().random}

# 发起网络请求
response = requests.get(url, headers=headers)

# 指定编码格式
response.encoding = 'utf-8'

# 保存
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
