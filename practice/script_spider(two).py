import requests
from bs4 import BeautifulSoup
import time

def parse_page(url):
    res = requests.get(url)
    print('响应状态码：', res.status_code)
    soup = BeautifulSoup(res.text, 'lxml')
    pics = soup.select('div[id=comments] > ul > li > div[class=comment-body] > p > img')
    for i in pics:
        src = i.get('src')
        pic_name = src.split('/')[-1]
        # pic_url = '/home/shiyanlou/Desktop/script_spider/{}'
        pic_url = 'C:/Users/Hus/Desktop/temp/{}'
        pic_res = requests.get(src)
        try:
            with open(pic_url.format(pic_name), 'wb') as f:
                f.write(pic_res.content)
            print(pic_name,'下载完成')
        except:
            print('图片无法保存，请在桌面上创建名为script_spider的文件夹')
            break
    print('结束爬取 -',url)



def main():
    res = requests.get('http://www.mzitu.com/zipai')
    soup = BeautifulSoup(res.text, 'lxml')
    num_list = soup.select("div[id='comments'] > div > span")
    num = num_list[1].get_text()
    base_url = "http://www.mzitu.com/zipai/comment-page-{}#comments"
    for i in range(1,int(num)):
        print('正在爬取 -',base_url.format(str(i)))
        parse_page(base_url.format(str(i)))
        time.sleep(2)

if __name__ == '__main__':
    main()
