# 通过params传参
import requests
from fake_useragent import FakeUserAgent

headers = {'User-Agent': FakeUserAgent().random}
word = input('请输入想要搜索的内容：')

# 定义网址并且通过params传参
url = "https://www.so.com/s"
params = {
    "ie": "utf-8",
    "fr": "360sou_newhome",
    "src": "home_none",
    "ssid": "29052cc2dd504871b3468da78988b18e",
    "sp": "a0b",
    "cp": "0630580045",
    "nlpv": "placeholder_base_dt_60",
    "q": word
}

# 发起网络请求并进行保存
response = requests.get(url, params=params, headers=headers)
with open(f'360-{word}-2.html', 'w', encoding='utf-8') as f:
    f.write(response.text)