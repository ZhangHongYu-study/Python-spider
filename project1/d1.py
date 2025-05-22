# requests库的一些基础用法
import requests

# 定义爬取网址
url = 'https://www.baidu.com'

# 发起网络请求
response = requests.get(url)

# 如果文本中出现乱码，需要对响应对象指定对应的字符集
response.encoding = 'utf-8'

# print(response)  # 可以得到服务器响应的状态码
# print(response.status_code)  # 得到响应对象的状态码
# response.headers得到响应头  response.request.headers得到请求头  response.cookies得到cookies信息

# 输出信息的几种方式
# print('==========================================')
# print(response.text)
# print('==========================================')
# print(response.content.decode('utf-8'))
# print('==========================================')
# print(response.content)
# print('==========================================')
