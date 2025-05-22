# 通过更改参数来修改搜索内容以360搜索为例
import requests
from fake_useragent import FakeUserAgent

# 定义请求头并规定搜索内容
headers = {'User-Agent': FakeUserAgent().random}
word = input('请输入想要搜索的内容:')

# 发起网络请求并进行保存
url = 'https://www.so.com/s?q=' + word
response = requests.get(url, headers=headers)
with open(f'360-{word}.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
