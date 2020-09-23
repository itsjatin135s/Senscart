from bs4 import BeautifulSoup as soup
from flask import url_for
import requests

def snapdeal(rawquery):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]

	query=rawquery.replace(" ","-")

	try:
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
		snapdeals = requests.get("https://www.snapdeal.com/search?keyword={}".format(query),headers=headers)
		soup1=soup(snapdeals.text,'lxml')
	
		j=soup1.find_all('source')
		for image in j:
			imglink.append(image['srcset'])
			

		k=soup1.find_all('span',{'class':'product-price'})
		for price in k:
			rs="₹"+price['display-price']
			prices.append(rs)
			

		l=soup1.find_all('p',{'class':'product-title'})
		for title in l:
			title1=title['title']
			title2=title1[0:33]+"..."
			producttitle.append(title2)
			

	
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