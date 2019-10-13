import requests
import json
import time

url = 'http://exercise.kingname.info/ajax_5_backend'

# 直接cv
html_json = requests.post(  url,
                            headers={'ReqTime': '1570970936135'},
                            json={'sum':'1'}).content.decode()
html_dict = json.loads(html_json)
print(html_dict)
# {'success': False, 'reason': '放弃吧，参数是有过期时间的，别想一个参数用到老。'}

# 生成时间戳
html_json = requests.post(  url,
                            headers={'ReqTime': str(int(time.time()*1000))},
                            json={'sum':'1'}).content.decode()
html_dict = json.loads(html_json)
print(html_dict)
# {'success': False, 'reason': '数据校验失败！'}

