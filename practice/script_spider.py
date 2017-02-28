import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.mzitu.com/zipai')
print('响应状态码：', res.status_code)
soup = BeautifulSoup(res.text, 'lxml')
pics = soup.select('div[id=comments] > ul > li > div[class=comment-body] > p > img')
print('抓取总数：', len(pics))
for i in pics:
    src = i.get('src')

    pic_name = src.split('/')[-1]
    pic_url = '/home/shiyanlou/Desktop/script_spider/{}'
    pic_res = requests.get(src)

    with open(pic_url.format(pic_name), 'wb') as f:
        f.write(pic_res.content)