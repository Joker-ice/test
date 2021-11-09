from base64 import encode
from re import S
import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
import json

# session = Session()
# session.post()
# r = requests.post(url='http://www.baidu.com')
a = {
    'url':'https://www.baidu.com',
    'headers': {"User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64)\
         AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"},
    # 'verify':False
    }
print(*a)
res = getattr(requests, 'get')(**a)
# # res = getattr(requests, 'post')(url='https://www.baidu.com')
# print(res.text)
res.encoding='utf8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.title)
