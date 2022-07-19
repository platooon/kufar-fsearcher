import requests
from bs4 import BeautifulSoup
import re

url = 'https://companies.devby.io/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
link = soup.find_all('a', href=True)

lst = []

for i in link:
    lst.append(re.findall('[href="/+"]', i))

print(lst)
