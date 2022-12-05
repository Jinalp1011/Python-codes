import json

data = '{"var1":"harry" , "var2":56}'
print(data)
parsed = json.loads(data)
print(type(parsed))