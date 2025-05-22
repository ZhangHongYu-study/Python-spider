# 通过requests来保存图片
import requests

url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

# 发起网络请求并保存
r = requests.get(url)
with open('image.png', 'wb') as f:
    f.write(r.content)
