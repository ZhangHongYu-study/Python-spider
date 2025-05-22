# 中文的编码
from urllib.parse import quote, unquote

word = '西瓜'
# 将文字编码
data = quote(word)
print(data)
# 将文字解码
info = unquote(data)
print(info)
