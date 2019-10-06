import lxml.html

html1 = '''
<html>
    <head lang = "en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <div id="test">
        我左青龙
            <span id="tiger">
                右白虎
                <ul>上朱雀
                    <li>下玄武</li>
                </ul>
                老牛在当中
            </span>
            龙头在胸口
        </div>
    </body>
</html>
'''

selector_1 = lxml.html.fromstring(html1) 
print(type(selector_1))
content_1 = selector_1.xpath('//div[@id="test"]/text()')
#for each in content_1:
#    print(each)
#        我左青龙
#
#
#            龙头在胸口


#先抓大再抓小
data = selector_1.xpath('//div[@id="test"]')[0]
info = data.xpath('string(.)')
print(type(data))
print(type(info))
#print(info)
#        我左青龙
#
#                右白虎
#                上朱雀
#                    下玄武
#
#                老牛在当中
#
#            龙头在胸口







