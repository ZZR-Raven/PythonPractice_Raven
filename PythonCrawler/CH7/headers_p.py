import requests
import json

url = 'http://exercise.kingname.info/exercise_headers_backend'

# html_json = requests.get(url).content.decode()
# html_dict = json.loads(html_json)
# print(html_dict)
# {'success': False, 'reason': '请不要使用爬虫访问本页面。'}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'anhao': 'kingname',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': '__cfduid=d4e57b017e839cd9751b84d23499714c11570949750',
    'DNT': '1',
    'Host': 'exercise.kingname.info',
    'Referer': 'http://exercise.kingname.info/exercise_headers.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
# chrome浏览器cv过来改个格式
html_json = requests.get(url,headers=headers).content.decode()
html_dict = json.loads(html_json)
print(html_dict)
# {'code': '访问成功，通关密码：38323', 'success': True}

headers_UA = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'anhao': 'kingname',
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json; charset=utf-8',
    # 'Cookie': '__cfduid=d4e57b017e839cd9751b84d23499714c11570949750',
    # 'DNT': '1',
    # 'Host': 'exercise.kingname.info',
    # 'Referer': 'http://exercise.kingname.info/exercise_headers.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}
# 某些网站只需要加上User-Agent 
html_json = requests.get(url,headers=headers_UA).content.decode()
html_dict = json.loads(html_json)
print(html_dict)
# {'success': False, 'reason': '你以为设个UA就能逃脱检查吗？'} 练习网站不行hh

