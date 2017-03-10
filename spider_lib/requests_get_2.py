import requests
import re
from bs4 import BeautifulSoup
res = requests.get('https://www.shiyanlou.com/courses/')
soup = BeautifulSoup(res.text, 'lxml')
course = soup.find_all('div',{'class':'col-md-4','class':'col-sm-6','class':'course'})
for i in course:
    title = i.find('div',{'class':'course-name'}).get_text()
    study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
    study_people = re.sub("\D", "", study_people)# 数字这里有太多的空格和回车，清理一下
    try:
        tag = i.find('span',{'class':'course-per-num','class':'pull-right'}).get_text()
    except:
        tag="课程"
    print("{}    学习人数:{}    {}\n".format(tag, study_people, title,))