import requests
res = requests.get('https://www.shiyanlou.com/courses/')
print(res.status_code)  # 200