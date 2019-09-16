import requests

res = requests.get('https://api.github.com/users/smithjunior')
data = res.json()
print(data)
