import requests
import lxml.html

url = 'http://exercise.kingname.info/exercise_captcha.html'
url_check = 'http://exercise.kingname.info/exercise_captcha_check'

session = requests.Session()
html = session.get(url).content
selector = lxml.html.fromstring(html)
captcha_url = selector.xpath('//img/@src')[0]

# 下载验证码文件
img = requests.get('http://exercise.kingname.info/' + captcha_url).content
with open('captcha.png','wb') as f:
    f.write(img)

captcha = input('手动查看chptcha.png，输入验证码')
after_check = session.post(url_check,data={'captcha':captcha})

print(f'输入验证码后网站返回：{after_check.content.decode()}')