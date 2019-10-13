import json
import re
import requests

url = 'http://exercise.kingname.info/exercise_ajax_3.html'
first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
second_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'

page_html = requests.get(url).content.decode()
secret_2 = re.search("secret_2 = '(.*?)'",page_html,re.S).group(1)
# print(secret_2)       #kingname

ajax_1_json = requests.get(first_ajax_url).content.decode()
ajax_1_dict = json.loads(ajax_1_json)
# print(ajax_1_dict)    #{'code': 'kingname is genius.', 'success': True}
secret_1 = ajax_1_dict['code']
# print(secret_1)       #kingname is genius.

ajax_2_json = requests.post(second_ajax_url,json = {'name':'Raven',
                                                    'age':19,
                                                    'secret1':secret_1,
                                                    'secret2':secret_2}).content.decode()

ajax_2_dict = json.loads(ajax_2_json)
code = ajax_2_dict['code']
print(f'最终显示的内容:{code}')
# 最终显示的内容:行动代号：哎哟不错哦


