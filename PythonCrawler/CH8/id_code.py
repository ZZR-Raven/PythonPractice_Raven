import requests
import lxml.html
import urllib3
urllib3.disable_warnings()

'static/captcha/1571406261.9589076.png'
url = 'http://exercise.kingname.info/exercise_capcha.html'
url_check = 'http://exercise.kingname.info/exercise_captcha_check'

session = requests.Session()
html = session.get(url).content
selector = lxml.html.fromstring(html)
captcha_url = selector.xpath('//img/@src')[0]

#下载验证码文件
image = requests.get('http://exercise.kingname.info/'+captcha_url).content
with open ('cap.png','wb')as f:
    f.writa(image)

captcha = input ('查看cap.png文件，人眼识别然后输入到这里')
after_check = session.post(url_check,data = {'captcha':captcha})

print(f'输入验证码以后 网站返回{after_check.content.decode()}')





