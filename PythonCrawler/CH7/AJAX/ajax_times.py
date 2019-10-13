import json
import requests

url = 'http://exercise.kingname.info/exercise_ajax_3.html'

return_json_1 = requests.post(url,json={'name':'raven',
                                        'age':19,
                                        'secret1':'2333',
                                        'secret2':'hhhh'})
                                        
return_json_2 = requests.post(url,json={'name':'raven',
                                        'age':19})
                    
print('乱写secret1跟secret2，返回:{json.loads(return_json_1.content.decode())}')
print('不写secret1跟secret2，返回:{json.loads(return_json_2.content.decode())}')
# 乱写secret1跟secret2，返回:{json.loads(return_json_1.content.decode())}
# 不写secret1跟secret2，返回:{json.loads(return_json_2.content.decode())}


#   secret_2可以从源代码找到
# <html>
#     <head>
#         <title>exercise ajax load</title>
#         <script> var secret_2 = 'kingname';</script>
#     </head>
#     <body>
#         <div class="content"></div>
#     </body>
#     <script src="static/js/jquery-3.2.1.min.js"></script>
#     <script src="static/js/loaddata_3.js"></script>
# </html>

# 其他请求ajax_3_backend 
# 可以找到secret1，名字是code
# {"code": "kingname is genius.", "success": true}
