import requests
import re
from bs4 import BeautifulSoup

host_url = "http://www.shiyanlou.com{}"

count = 0
def get_course_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    # soup = BeautifulSoup(html, 'lxml')
    course = soup.find_all('div', {'class': 'col-md-4', 'class': 'col-sm-6', 'class': 'course'})
    for i in course:
        global count
        count = count + 1
        href = i.find('a',{'class':'course-box'}).get('href')
        title = i.find('span', {'class': 'course-title'}).get_text()
        study_people = i.find('span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
        study_people = re.sub("\D", "", study_people)  # 数字这里有太多的空格和回车，清理一下
        try:
            tag = i.find('span', {'class': 'course-per-num', 'class': 'pull-right'}).get_text()
        except:
            tag = "课程"
        print("{}    学习人数:{}    {}   课程链接:{}\n".format(tag, study_people, title,host_url.format(href) ))

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
        # print(course_link.format(i))
        get_course_link(course_link.format(i))


if __name__ == "__main__":
    main()
    print("课程总数：{}".format(count))
    # get_course_link('www.demo.com')