import requests

response = requests.get(f"https://en.wikipedia.org/robots.txt")

r_txt = response.text

print(r_txt)