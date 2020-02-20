import bs4,requests

a=str(input("enter product:- "))
res = requests.get("https://www.flipkart.com/search?q={}",format(a))
soup = bs4.BeautifulSoup(res.text,'lxml')
#for i in soup.select('src',{"class":"_3liAhj"}):
print(soup)







	