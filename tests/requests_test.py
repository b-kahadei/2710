import requests

url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"

req = requests.get(url)

print(req.text)