import requests
import re
from bs4 import BeautifulSoup
import time

host_url = "http://www.shiyanlou.com{}"

def write_file(string):
    log = open('/home/shiyanlou/Desktop/shiyanlou_spider.log','a')
    log.write(string+'/n')
    log.close()

def parse_content(url, title, tag, study_num):
    print(url, '&' * 10)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    type_list = soup.select('ol[class=breadcrumb] > li > a')
    types = []
    for i in type_list:
        if type_list.index(i)!=0 and type_list.index(i)!=len(type_list)-1:
            types.append(i.get_text())
    info = soup.find('div',{'class':'course-infobox-content'})
    try:
        info = info.find('p').get_text()
    except:
        info = "无介绍"
    teacher = soup.find('div',{'class':'name'})
    try:
        teacher = teacher.find('strong').get_text()
    except:
        teacher = "匿名"
    labs = soup.find('div',{'id':'labs'})
    test_list = labs.find_all('div',{'class':'lab-item'})
    tests_name = []
    for i in test_list:
        name = i.find('div',{'class':'lab-item-title'}).get_text()
        tests_name.append(name)
    write_file("课程名：{}    老师：{}    tag:{}    学习人数：{}    类型：{}".format(title,teacher,tag,study_num,'&'.join(types)))
    write_file("简介：{}".format(info))
    for i in tests_name:
        write_file(i)
    write_file('*'*100)



def get_course_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    course = soup.find_all('div', {'class': 'col-md-4', 'class': 'col-sm-6', 'class': 'course'})
    for i in course:
        href = i.find('a',{'class':'course-box'}).get('href')
        title = i.find('span', {'class': 'course-title'}).get_text()
        study_people = i.find('span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
        study_people = re.sub("\D", "", study_people)  # 数字这里有太多的空格和回车，清理一下
        try:
            tag = i.find('span', {'class': 'course-per-num', 'class': 'pull-right'}).get_text()
        except:
            tag = "课程"
        parse_content(url=host_url.format(href),title=title,tag=tag,study_num=study_people)
        time.sleep(0.5)

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
    for i in range(1,page_num+1):
        get_course_link(course_link.format(i))


if __name__ == "__main__":
    main()


