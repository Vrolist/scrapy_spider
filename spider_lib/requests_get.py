import requests
res = requests.get('https://www.shiyanlou.com/')
print(res.status_code)  # 200