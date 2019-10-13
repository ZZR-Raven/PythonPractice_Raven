import json
import requests
import re

url = 'http://exercise.kingname.info/exercise_ajax_2.html'
html = requests.get(url).content.decode()
# print(html)

# ###########为什么是secret呢##############
code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
print(code_json)
code_dict = json.loads(code_json)
print(code_dict['code'])






