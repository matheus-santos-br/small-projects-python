import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

r = requests.get(url)

#print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find_all("h2", {"class": "post-title"})

#print(titles)
#print(titles[0].getText())

for aux in titles:
    print(aux.getText())