from base64 import encode
from re import S
import requests
from bs4 import BeautifulSoup


class ApiRequest():
    def to_request(self, url):
        data = {
            'url':url,
            'headers': {"User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64)\
                AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"},
            }
        res = getattr(requests, 'get')(**data)
        res.encoding='utf8'
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.title)

    def get_url(self):
        for i in range(0,10):
            url = 'https://movie.douban.com/top250?start=' + str(i*25)
            self.to_request(url)
            print(url)
if __name__ == '__main__':
    a = ApiRequest()
    a.get_url()