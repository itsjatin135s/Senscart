from bs4 import BeautifulSoup as soup
from pyquery import PyQuery as jQ
import json
import codecs
from flask import url_for


def amazon(query):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]


	try:
		file="amazon{}.html".format(query)
		opener=codecs.open( file , 'r','utf-8-sig')
		read=opener.read()
		soup1=soup(read,'lxml')



		limit=0
		j=soup1.find_all('img',{'class':'s-image'})
		for image in j:
			limit = limit+1
			if limit<=11:
				if limit ==1:
					pass
				else:
					imglink.append(image['src'])
			else:
				break


		limit1=0
		k=soup1.find_all('span',{'class':'a-price-whole'})
		for image in k:
			limit1 = limit1+1
			if limit1<=11:
				if limit1==1:
					pass
				else:
					rs=("₹"+image.text)
					prices.append(rs)
			else:
				break



		limit2=0
		l=soup1.find_all('img',{'class':'s-image'})
		for image in l:
			limit2 = limit2+1
			if limit2<=11:
				if limit2 ==1:
					pass
				else:
					title1=image['alt']
					title2=title1[0:33]+"..."
					producttitle.append(title2)
			else:
				break




		limit3=0
		m=soup1.find_all('a',{'class':'a-link-normal s-no-outline'})
		for image in m:
			limit3 = limit3+1
			if limit3<=11:
				if limit3 ==1:
					pass
				else:
					productlink.append('https://amazon.in'+image['href'])
			else:
				break

	except :
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")


	return(zip(imglink,prices,producttitle,productlink))