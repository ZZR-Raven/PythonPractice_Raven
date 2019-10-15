# import re
# import json
# import requests

# class letvspider(object):
#     comment_url = '''https://control-i.iqiyi.com/control/content_config
#                     ?albumid=0&block=B&business=like&categoryid=
#                     &is_iqiyi=true&is_video_page=true&qypid=340992
#                     &rpage=aHR0cHM6Ly93d3cuaXFpeWkuY29tL3ZfMTlydTRxeGlxYy5odG1s&s2=aHR0cHM6Ly93d3cuaXFpeWkuY29tL2RpYW55aW5nLw%3D%3D
#                     &tvid=7854817400
#                     &uid=0&version=1.0.0&callback=jsonp_1571153470846_64378'''

#     headers = {
#                 ':authority': 'www.iqiyi.com',
#                 ':method': 'GET',
#                 ':path': '/v_19ru4qxiqc.html',
#                 ':scheme': 'https',
#                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#                 'accept-encoding': 'gzip, deflate, br',
#                 'accept-language': 'zh-CN,zh;q=0.9',
#                 'cache-control': 'max-age=0',
#                 'cookie': 'QC005=746648585fec540a482319f291e0b966; QC173=0; QC007=DIRECT; QC006=691fr89ww2nwyfa64xf3drrn; QC008=1571153420.1571153420.1571153420.1; nu=0; QYABEX={"pcw_home_movie":{"value":"old","abtest":"146_A"}}; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1571046767,1571050504,1571153420; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D; T00404=47f602a6359bf4b88a453e82ed6f67cc; QC176=%7B%22state%22%3A0%2C%22ct%22%3A1571153442005%7D; QP001=1; QP0013=; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1571153458; QC179=%7B%22userIcon%22%3A%22//www.iqiyipic.com/common/fix/site-v4/header-userImg-default-green.png%22%7D; T00700=EgcIysDtIRAB; CA0001=%7B%22code%22%3A%22b20f64bd520f631bA00000%22%2C%22type%22%3A132%2C%22detail%22%3A%7B%22fv%22%3A%22%22%2C%22text1%22%3A%22%E9%A6%96%E6%9C%88%E4%BB%858%E5%85%83%22%2C%22autoRenew%22%3A%22true%22%2C%22type1%22%3A%7B%22vipType%22%3A%229c4e4c1c18827a41%22%2C%22type%22%3A%225%22%2C%22fc%22%3A%2290647efdbbc99688%22%7D%2C%22packageAmount%22%3A%221%22%7D%2C%22passportId%22%3A%22%22%2C%22locale%22%3A%22cn%22%7D; __uuid=e3d5add9-9a42-498c-e8ca-e9ff9ae5fbb1; QC010=211162897; QILINPUSH=1; QP0022=CERNET%7CGuangDong_GuangZhou_scut_IOCP-221.4.34.65%7Ciocp_guangdong_guangzhou_scut_cernet%7C0; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A13%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%7D; IMS=IggQARj_2ZftBSokCiAzNDk4MjQ4MzM1YWI5NDdjNTExZDZjNGNkZTY1NmFkNRAA; QP007=540; __dfp=a089c95583edc04b82ba0ff5a9f4f1772bcf879d733070552596a0855f35a6948e@1572342772758@1571046773758; TQC002=type%3Djspfmc140109%26pla%3D11%26uid%3D746648585fec540a482319f291e0b966%26ppuid%3D%26brs%3DCHROME%26pgtype%3Dplay%26purl%3Dhttps%3A%252F%252Fwww.iqiyi.com%252Fv_19ru4qxiqc.html%26cid%3D1%26tmplt%3D%26tm1%3D16262%2C0',
#                 'dnt': '1',
#                 'referer': 'https://www.iqiyi.com/dianying/?vfrm=pcw_home&vfrmblk=C&vfrmrst=712211_channel_dianying',
#                 'upgrade-insecure-requests': '1',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
#     }

#     def __init__(self,url):
#         self.necessary_info = {}
#         self.url = url
#         self.get_necessary_id()
#         self.get_comment()

#     def get_source(self,url,headers):
#         return requests.get(url,headers).content.decode()

#     # @staticmethod
#     def get_necessary_id(self):
#         # source = self.get_source(self.url,self.headers)
#         # vid = re.search(r'vid: (\d+)',source).group(1)
#         # pid = re.search(r'pid: (\d+)',source).group(1)
#         self.necessary_info['tvid'] = 7854817400#vid
#         self.necessary_info['pid'] = 340992 #pid

#     def get_comment(self):
#         # self.url = self.comment_url.format(#tvid=self.necessary_info['tvid'],
#         #                               pid=self.necessary_info['pid'])
#         # print(self.url)
#         source = self.get_source(self.url,self.headers)
#         source_json = source[source.find('{"'): -1]
#         comment_dict = json.loads(source_json)
#         comments = comment_dict['data']
#         for comment in comments:
#             print(f'发帖人:{comment["user"]["username"]}, 评论内容：{comment["content"]}')

# if __name__ == '__main__':
#     spider = letvspider('https://static.iqiyi.com/js/common/mars_v.js?1571153466207')

