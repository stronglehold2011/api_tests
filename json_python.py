import json
json_data = '{"name":"Иван","age": 30,"is_student":"false" }'   # это еще строка


parsed_data = json.loads(json_data)
print(parsed_data, type(parsed_data))


