import re
import json
import requests

class letvspider(object):
    comment_url = '''https://control-i.iqiyi.com/control/content_config
                    ?albumid=0&block=B&business=like&categoryid=
                    &is_iqiyi=true&is_video_page=true&qypid=01010011010000000000
                    &rpage=aHR0cHM6Ly93d3cuaXFpeWkuY29tL3ZfMTlydTRxeGlxYy5odG1s&s2=aHR0cHM6Ly93d3cuaXFpeWkuY29tL2RpYW55aW5nLw%3D%3D
                    &tvid=7854817400
                    &uid=0&version=1.0.0&callback=jsonp_1571153470846_64378'''

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'tj_lc=0c1fd037e3612ae23a33023d8130fd6b; tj_uuid=-_15710366234085941215; tj_env=1; ssoCookieSynced=1; tj2_lc=ef6549df49eadbb51106e26aa1a62222; ark_uuid=ck-59c20d24-2b08-494e-b162-fd34bff232d5-1014-150344; bd_xid=0c1fd037e3612ae23a33023d8130fd6b; language=zh-cn; sso_curr_country=CN; sourceUrl=http%3A%2F%2Fwww.le.com%2F; tj_v2c=-31637808_1-31634358_1-31637715_1-31611235_5-31545092_1-31639140_1',
        'DNT': '1',
        'Host': 'www.le.com',
        'Referer': 'http://movie.le.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    }

    def __init__(self,url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    def get_source(self,url,headers):
        return requests.get(url,headers).content.decode()

    # @staticmethod
    def get_necessary_id(self):
        # source = self.get_source(self.url,self.headers)
        # vid = re.search(r'vid: (\d+)',source).group(1)
        # pid = re.search(r'pid: (\d+)',source).group(1)
        self.necessary_info['tvid'] = 7854817400#vid
        self.necessary_info['pid'] = 340992 #pid

    def get_comment(self):
        # self.url = self.comment_url.format(tvid=self.necessary_info['tvid'],
        #                               pid=self.necessary_info['pid'])
        print(self.url)
        source = self.get_source(self.url,self.headers)
        source_json = source[source.find('{"'): -1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人:{comment["user"]["username"]}, 评论内容：{comment["content"]}')

if __name__ == '__main__':
    spider = letvspider('https://static.iqiyi.com/js/common/mars_v.js?1571153466207')

