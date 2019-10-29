import pytesseract
from PIL import Image

image = Image.open('captcha.png')
# image.load()        #加载一下图片
# image.show() 
code = pytesseract.image_to_string(image)
print(code)







