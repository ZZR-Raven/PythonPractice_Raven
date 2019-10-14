from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
time.sleep(5)
html = driver.page_source
print(html)
#
# DevTools listening on ws://127.0.0.1:50131/devtools/browser/8fca5b75-e1ee-407d-a641-5144fe165259
# <html xmlns="http://www.w3.org/1999/xhtml"><head>
#         <title>exercise ajax load</title>
#     </head>
#     <body>
#         <div class="content">通关成功，通关口令：这是最终数据。</div>

#     <script src="static/js/jquery-3.2.1.min.js"></script>
#     <script src="static/js/exercise_check.js"></script>
# </body></html>








