from bs4 import BeautifulSoup as soup
from pyquery import PyQuery as jQ
import json
import codecs
from flask import url_for
import requests

def flipkart(query):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]


	try:
		# file="flipkart{}.html".format(query)
		# opener=codecs.open(file, 'r','utf-8-sig')
		# read=opener.read()
		# query= jQ(read)


		# script=query("#is_script").text()
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
		f=requests.get("https://flipkart.com/search?q={}".format(query),headers=headers)
		ft=soup(f.content,'lxml')
		fk=ft.find('script',id='is_script').text

		remove1=fk.replace('window.__INITIAL_STATE__ = ','')
		remove2=remove1[:-2]
		k1=json.loads(remove2)
		# print(k1)
		for x in range(1,11):
			j=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['media']['images'][0]['url'])
			width=j.replace("{@width}","250")
			height=width.replace("{@height}","250")
			final=height.replace("{@quality}","70")
			imglink.append(final)
			print(final)
		
		for x in range(1,11):
			l=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['pricing']['finalPrice']['decimalValue'])
			rs="₹"+l
			prices.append(rs)
			print(rs)

		for x in range(1,11):
			m=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['smartUrl'])
			productlink.append(m)
			print(m)


		for x in range(1,11):
			n=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['titles']['title'])
			o=n[0:33]+"..."
			producttitle.append(o)
			print(o)

	except:
		# print(script)
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")
		print("hey buddy here i am")

	return(zip(imglink,prices,producttitle,productlink))

# print(imglink)
# print(prices)
# print(product)
# print(productlink)



