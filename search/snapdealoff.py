import requests
from bs4 import BeautifulSoup as soup



def snapoff():
	photo=[]
	title1=[]
	productlink=[]
	discount=[]

	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
	snapdeals = requests.get("https://www.snapdeal.com/",headers=headers)
	soup1=soup(snapdeals.text,'lxml')

	
	m=soup1.find_all('div',{'class':'product-img preLoadBackgr'})
	for div in m:
		l=div.find_all('img',{'class':'lazy-load'})
		for image in l:
			photo.append(image['data-src'])
			# print(image['data-src'])
	n=soup1.find_all('a',{'class':'product-card dp-widget-link'})
	for link in n:
		productlink.append(link['href'])

	o=soup1.find_all('div',{'class':'product_name'})
	for title in o:
		tit=title.text[0:33]+"..."
		title1.append(tit)

	p=soup1.find_all('div',{'class':'product_disc'})
	for disc in p:
		discount.append(disc.text)
		
	return(photo,title1,productlink,discount)