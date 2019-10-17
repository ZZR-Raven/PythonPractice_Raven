import requests
import urllib3
urllib3.disable_warnings()

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_zap=818b9b9c-f28f-4a25-8902-68f70b733009; d_c0="ABCi1n4g_w-PTg_mKHGKD3kZS_cLNpUXYGI=|1567599316"; _xsrf=b3kRdfRzMHu2nwqLDUob5yXTZpx127eY; tst=r; tgw_l7_route=060f637cd101836814f6c53316f73463; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1570849198,1570979005,1571022428,1571320019; capsion_ticket="2|1:0|10:1571320020|14:capsion_ticket|44:ZDk1NTFjYWI2Yzg4NDRhZDhmZjA5MTlhYmU1N2JiNDM=|d498400414c1dc9a1f9ae46196429ed31ba2a08c995736e985c87e0e14acec6a"; z_c0="2|1:0|10:1571320024|4:z_c0|92:Mi4xT3htRUJ3QUFBQUFBRUtMV2ZpRF9EeVlBQUFCZ0FsVk4yTDZWWGdCbHR6aEtFM20zNGx0RTRYemdQOVI1dE1lWENn|0edbade94bddfef85e29b7b07718dad9fb31a487ef746c62c12ed9a6a3ce633c"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1571320026',
    'dnt': '1',
    'referer': r'https://www.zhihu.com/signin?next=%2F',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

session = requests.Session()
source = session.get('https://www.zhihu.com',headers=header,verify=False).content.decode("utf-8","ignore")
# print(source)


