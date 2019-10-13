import json


person = {
        'basic_info': {'name': '哈哈哈',        #unicode
                'age': 24,
                'sex': 'male',
                'merry': False},
        'work_info': {'salary': 99999,
                'position': 'engineer',
                'department': None}
}

# 转换成json格式
person_json = json.dumps(person)
# print(person_json)

# 插入空格indent
person_json_indent = json.dumps(person,indent=4)
# print(person_json_indent)


















































