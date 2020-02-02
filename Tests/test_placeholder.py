import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
print(response.text)
     #print((response.json()[1]['state']) == 'Ohio')
