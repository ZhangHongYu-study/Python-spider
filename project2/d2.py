# 通过更改参数内容来下载网易云歌曲
import requests
from fake_useragent import FakeUserAgent

# 定义请求头
headers = {'User-Agent': FakeUserAgent().random}

# 通过改变歌曲的id来进行下载不同歌曲
music_id = input('请输入歌曲id：')
url = "https://music.163.com/song/media/outer/url?id=" + music_id
response = requests.get(url, headers=headers)
with open('music.mp3', 'wb') as f:
    f.write(response.content)
