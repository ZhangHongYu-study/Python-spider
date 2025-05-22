# 参数在url中的作用以百度搜索为例
import requests
from fake_useragent import FakeUserAgent

headers = {'User-Agent': FakeUserAgent().random}
url = 'https://www.baidu.com/s?wd=%E4%BD%A0%E5%A5%BD'  # 大多网址其内容只与特定参数有关
r = requests.get(url, headers=headers)
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
