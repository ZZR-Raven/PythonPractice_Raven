import re
import json
import requests

class letvspider(object):
    comment_url = '''   
                https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_pre_authentication
                &cmd=24792&callback=jQuery19105484692978224748_1571304597297
                &platform=2&cid=qviv9yyjn83eyfu&vid=l00173o64p7&type=0&isVip=false&_=1571304597298                
                '''

    headers = {
                # :authority: v.qq.com
                # :method: GET
                # :path: /x/cover/qviv9yyjn83eyfu/l00173o64p7.html
                # :scheme: https
                # accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
                # accept-encoding: gzip, deflate, br
                # accept-language: zh-CN,zh;q=0.9
                # cache-control: max-age=0
                # cookie: tvfe_boss_uuid=b869173e19a387cb; pgv_pvid=4979822624; pgv_info=ssid=s9014709888; ts_refer=cn.bing.com/; ts_uid=7190010790; bucket_id=0; video_guid=03df4259b4041dc5; video_platform=2; ptag=cn_bing_com|detail; ts_last=v.qq.com/x/cover/qviv9yyjn83eyfu/l00173o64p7.html; qv_als=Cb85u6Prl5JiCCJdA11571304569SZjVGQ==; ad_play_index=6
                # dnt: 1
                # if-modified-since: Thu, 17 Oct 2019 09:20:00 GMT
                # referer: http://v.qq.com/detail/q/qviv9yyjn83eyfu.html
                # upgrade-insecure-requests: 1
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
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
        # self.necessary_info['xid'] = vid
        # self.necessary_info['pid'] = pid
        pass

    def get_comment(self):
        self.url = self.comment_url#.format(xid=self.necessary_info['xid'],
                                    #  pid=self.necessary_info['pid'])
        print(self.url)#
        source = self.get_source(self.url,self.headers)
        source_json = source[source.find('{"'): -1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人:{comment["user"]["username"]}, 评论内容：{comment["content"]}')

if __name__ == '__main__':
    spider = letvspider('https://v.qq.com/x/cover/qviv9yyjn83eyfu/l00173o64p7.html')

# '''
# http://api.my.le.com/vcm/api/list?jsonp=jQuery19102629000432028177_1571305451394&type=video&rows=20&page=1&sort=&cid=1&source=1&xid=31637808&pid=10043181&ctype=cmt%2Cimg%2Cvote&listType=1&_=1571305451399
# '''

