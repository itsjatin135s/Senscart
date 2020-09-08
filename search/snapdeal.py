import codecs
from bs4 import BeautifulSoup as soup
from flask import url_for


def snapdeal(query):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]

	try:
		file="snapdeal{}.html".format(query)
		opener=codecs.open(file, 'r','utf-8-sig')
		read=opener.read()
		soup1=soup(read,'lxml')
	
		j=soup1.find_all('source')
		for image in j:
			imglink.append(image['srcset'])
			# print(image['srcset'])

		k=soup1.find_all('span',{'class':'product-price'})
		for price in k:
			rs="₹"+price['display-price']
			prices.append(rs)
			# print(price['display-price'])

		l=soup1.find_all('p',{'class':'product-title'})
		for title in l:
			title1=title['title']
			title2=title1[0:33]+"..."
			producttitle.append(title2)
			# print(title['title'])

	
		m=soup1.find_all('div',{'class':'product-desc-rating'})
		for link1 in m:
			n=link1.find_all('a',{'class':'dp-widget-link'})
			for link in n:
				productlink.append(link['href'])
				
	except:
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")




	return(zip(imglink,prices,producttitle,productlink))