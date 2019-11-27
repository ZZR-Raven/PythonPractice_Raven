import xlrd 

workbook=xlrd.open_workbook('amzuser.xlsx')
# print (workbook.sheet_names())
userinfo = workbook.sheet_by_name('Sheet1')
cell_value = userinfo.cell(1, 1).value
print(cell_value)
# cell_A = userinfo.cell(1,1).value print(cell_A) 

coo_1 = '''
skin=noskin; 
session-id=130-5304808-8042547; 
session-id-time=2082787201l; 
i18n-prefs=USD; 
lc-main=zh_CN; 
sp-cdn="L5Z9:CN"; 
ubid-main=130-6114388-0935861; 
x-wl-uid=1FAZ+GZcBqDtwRFVlMLPyTp7hejEdrNcrwNkSXuHlx3fy2sZvxD7IS5lmdun24/VkwD/rrEdc2+4=; 

session-token=2neBng4LLhSXYXkPZBdtxOCaVlFLTvE26Y5JdMbRrp3hBqJzk25Ar/beJxtsgTBvvjYfKEgbAGBVIt2FekWOAeBJ/0r75oahlPCvsBm1EE8BE6cLnPSvUaeSCyA0fSVFd0Xm9fPRdWmzXtAuLaUdp6m3FPsiFAagoRb3X0aRvOkj00Zkp9K5/M1MGpt0wEZLXnj+SClqckXsuFPxEe8BlN1x8bGpbKIQls86hNteYkb5pqDfr3hA3QPvMV4t48uC; 
csm-hit=tb:BY0FFA2DS86RN8EKKKFH+s-BY0FFA2DS86RN8EKKKFH|1574576400579&t:1574576400579&adb:adblk_no'''

coo_3 = '''
skin=noskin; 
session-id=130-5304808-8042547; 
session-id-time=2082787201l; 
lc-main=zh_CN; 
sp-cdn="L5Z9:CN"; 
ubid-main=130-6114388-0935861; 
x-wl-uid=1FAZ+GZcBqDtwRFVlMLPyTp7hejEdrNcrwNkSXuHlx3fy2sZvxD7IS5lmdun24/VkwD/rrEdc2+4=; 

csm-hit=tb:BY0FFA2DS86RN8EKKKFH+s-3DWQWBRVHMTHVRP8V4JE|1574576509102&t:1574576509102&adb:adblk_no; 
a-ogbcbff=1; session-token="oB6melPlPzSKWS54KRhoJKN+kORNfrtU6k7tV6Jb0lqMtmW4RSPXJPngSEGhtp2EEKN0sgHxUHNvMZ3AapODFpFUZXTkOgPc8FHnUJ1lzwjqJpsRq8xYu1cU+SUrZRKAE/eTUB2Q6mzQKYYi9lQH8Wl9Sf+maeHLNi0x45rq5ldB1i2L544USooa5AuFj/d26YhYjSU+DBcYsFK8TdjZ/knLJBNWOMv1gErhVe6G3gzSaNtQWeGeYXeDWCvQSEUx6o7c09esaS86i4VHgYM4pg=="; x-main="f1XuYAfyuewtsfehnDHEYRNUOIOb9??ynpOdtX5SmXtn8@jZrzy2jBsdqoXvpneN"; 
at-main=Atza|IwEBIAVxBEo5paP3gyRe3XlYsIa4kyKPAJNXIpPqQWOSLeD4RzQcvbcUcWWDO8Bn9ggl3KALbnVO2Zj6SJiRBOQuxT9LD7Ba3LD9ThVu-pGaP4Jryf0e9A6o1C4Q7rzEwUDXEw0LKY_o6TB1BdCaqviyksHZ9zOCj-sBrVSWVGMVjtGymM3hIy9k2Bpz19A4B9heRk5yR3qlEEZbypT_1a3gBBLS12IVlHgPXPbNeK0yratlz_38BObm36tJ5w617jtT8J9O-bOppkmOqUll9dxBp9_gAQ2XxF_UaumkyZO-SIja6JmlVj2Cr7pWydbxpuqUh7WyBD4eA40LNbvJTuSYtebMdA-xqymWTij9tloqq18Pbj43_l_O-Wwchke2nKV1O_IHgGqLXn45LBie32POukB0NebEpzvY50yqn5XmyTFOKltY7OFmQxnwfYmE7DA9osw; sess-at-main="VMyMoF61lmlnEz8/ezWrUUW9jodrmNfc2oiBmh9Dm4Q="; 
sst-main=Sst1|PQEKgY2c0gP2FxkWLSZclz7fCxqgKI5oX6phor2tgiEi8UpFMVbYJ54CdA-E9o47u0RQYCGE04qI2La-lDzeMjsX7c1Oq5vgTPqFZuyqCZaHt0WNLLVdvPLgVF9GuH5aMDGoA-LKz9eaxIijDPXvGGEQuGF2huHsXERNxuBdneDnqQq_r2I-w2TdrDo8TZN8SGmycCXYnwIn1BhUjW-t98bNhuMoHWbJ3qneJwX44TTKMZea9KC_kkauhYGnMEPjqEkoLovoGY1zxIWy4oyfXYJC16wlDlrCATDrniq8sKFGhrnMGf8D3InwJ4ooV_3pX6e8_d8lT-EaertZr-V4PcdtqA'''

# browser.save_screenshot('f://a.png')
# #截取当前网页，该网页有我们需要的验证码
# yzm=browser.find_element_by_id("captcha_img_id") 
# #定位验证码
# location=yzm.location
# #获取验证码x,y轴坐标
# size=yzm.size
# #获取验证码的长宽
# rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
# #截取的位置坐标
# i=Image.open("f://a.png") 
# #打开截图
# frame4=i.crop(rangle)
# #使用Image的crop函数，从截图中再次截取我们需要的区域
# frame4.save('f://frame4.jpg')
# #将截取到的验证码保存为jpg图片
# qq=Image.open('f://frame4.jpg')
# #打开jpg验证码图片
# text=pytesseract.image_to_string(qq).strip() 
# #使用image_to_string识别验证码
# browser.find_element_by_name("turing").send_keys(text)
# #将识别的图片验证码信息输入到验证码输入文本框中
# browser.find_element_by_class_name("btn").click()
# #点击登录按钮
