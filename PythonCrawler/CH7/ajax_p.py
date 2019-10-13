import json
import requests
import re

url = 'http://exercise.kingname.info/exercise_ajax_2.html'
html = requests.get(url).content.decode()
code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
code_dict = json.loads(code_json)
print(code_dict['code'])






