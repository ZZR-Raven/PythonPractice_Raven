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
                </ul>>
                老牛在当中
            </span>
            龙头在胸口
        </div>
    </body>
</html>
'''

selector_1 = lxml.html.fromstring(html1) 
content_1 = selector_1.xpath('//div[@id="test"]/text()')
for each in content_1:
    print(each)
#        我左青龙
#
#
#            龙头在胸口





