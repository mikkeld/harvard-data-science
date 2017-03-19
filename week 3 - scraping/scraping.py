import requests
from bs4 import BeautifulSoup

req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")
page = req.text
soup = BeautifulSoup(page, 'html.parser')

print(soup.title)