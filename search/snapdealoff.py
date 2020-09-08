import scrapy
import os
from bs4 import BeautifulSoup as soup
import codecs
import json
from pyquery import PyQuery as jQ


def snapoff():
	photo=[]
	title1=[]
	productlink=[]
	discount=[]

	# snapdeal=os.system("scrapy fetch --nolog https://www.snapdeal.com > snapdealoffer.html")

	opener1=codecs.open("snapdealoffer.html", 'r','utf-8-sig')
	read1=opener1.read()
	soup1=soup(read1,'lxml')
# print(soup1)
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