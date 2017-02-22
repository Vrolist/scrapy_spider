import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.shiyanlou.com/courses/')
soup = BeautifulSoup(res.text, 'lxml')
course = soup.find_all('div',{'class':'col-md-4 col-sm-6  course'})
print(course)