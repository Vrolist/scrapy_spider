import requests
import re
from bs4 import BeautifulSoup


host_url = ""
def main():
    res = requests.get('https://www.shiyanlou.com/courses/')
    soup = BeautifulSoup(res.text, 'lxml')
    course_link = "https://www.shiyanlou.com/courses/?course_type=all&tag=all&fee=all&page={}"
    page = soup.find_all('ul',{'class':'pagination'})
    if len(page)<1:
        print('未获得全部页面')
        return None
    li_num = page[0].find_all('li')
    page_num = 0
    for i in li_num:
        try:
            li_num = int(i.find('a').get_text())
        except:
            li_num = 0
        if li_num > page_num:
            page_num = li_num
    # print(page_num,type(page_num))
    for i in range(1,page_num+1):
        # print(i)
        get_course_link(course_link.format(i))

def get_course_link(url):
    print(url)


if __name__ == "__main__":
    main()