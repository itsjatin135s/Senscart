import scrapy
import os
from bs4 import BeautifulSoup as soup
import codecs
import json
from pyquery import PyQuery as jQ

def amzoff():
	photo=[]
	productink=[]
	title=[]
	amazon=os.system("scrapy fetch --nolog https://www.amazon.in > amazonoffer.html")
	#----amazon offer shower
	opener=codecs.open("amazonoffer.html", 'r','utf-8-sig')
	read=opener.read()
	soup1=soup(read,'lxml')



	limit=0
	j=soup1.find_all('img',{'class':'product-image'})
	for image in j:
		if limit<6:
			limit=limit+1
			photo.append(image['src'])
			tit=image['title'][0:33]+"..."
			title.append(tit)

		else:
			break

	limit1=0
	j=soup1.find_all('div',{'class':'deals-shoveler-card-image'})
	# print(j)
	for image in j:
		k=image.find_all('a')
		if limit1<6:
			for image1 in k:
				limit1=limit1+1
				productink.append("https://amazon.in"+image1['href'])
		else:
			break
	return(zip(photo,productink,title))