import requests
from bs4 import BeautifulSoup

url = requests.get("http://flipkart.com")

soup = BeautifulSoup(url.text,'lxml')

imgs = soup.find_all("div", {"class":"_3ZJShS_31bMyl"})
for img in imgs:
         print(img)

for link in so.find_all('_3togXc'):
...     print(link.get('src'))