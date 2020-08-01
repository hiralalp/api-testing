import requests
import json
import jsonpath


url="https://reqres.in/api/users/2"




file=open("test.json","r")

json_input=file.read()

request_json=json.loads(json_input)



response=requests.put(url,request_json)

print(response.content)



response_json=json.loads(response.text)

print(response_json)


