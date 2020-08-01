import requests
import json
import jsonpath


url="https://reqres.in/api/users"




file=open("test.json","r")

json_input=file.read()

request_json=json.loads(json_input)



response=requests.post(url,request_json)

print(response.content)



response_json=json.loads(response.text)


id=jsonpath.jsonpath(response_json,"id")

print(id[0])



