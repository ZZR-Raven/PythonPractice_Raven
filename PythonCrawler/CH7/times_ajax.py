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


