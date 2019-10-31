import requests


headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.264240818.1572489663; _gid=GA1.2.623807757.1572489663; BAIDU_SSP_lcr=https://cn.bing.com/; __utma=253067679.264240818.1572489663.1572489666.1572489666.1; __utmc=253067679; __utmz=253067679.1572489666.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmv=253067679.|1=Is%20Registered=No=1^3=ad_block=No=1; __utmb=253067679.7.10.1572489666; _32382_access_token=6a9b68f83ffc57c661e572389c7ccfa9861c5cde8cf9e6621caa7e8eea339cfb; _32382_ukey=odwvk3; _32382_auto_signin=1; _32353_access_token=83f7e8f9061a4b1a616ec533b26acc20b5a89b8e1f6069221e8c570bb5e0ae3d; _32353_ukey=odwvk3',
            'DNT': '1',
            'Host': 'www.guokr.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'

}

gkurl = 'https://www.guokr.com/'

session = requests.Session()
source = session.get(gkurl,headers=headers,verify=False).content.decode(encoding = 'utf-8',errors = 'ignore')
# print(source)
html = open('gk.html','w',encoding='utf-8')
html.write(source)


