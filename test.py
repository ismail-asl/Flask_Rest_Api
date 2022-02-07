import requests

BASE = "http://127.0.0.1:5000/"

#get data
response = requests.get(BASE + "video/10")
print(response.json())

#patch or update data
# response = requests.patch(BASE + "video/1",{"name":"New Name"})
# print(response.json())

#add or post data
# response = requests.post(BASE + "video/",{'name': 'post name', 'views': 33000, 'likes': 25000})
# print(response.json())