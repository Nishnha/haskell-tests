import requests as req

params = {'m':True}
response = req.get('http://wttr.in/Atlanta', params=params)
print(response.url)
print(response.text)
