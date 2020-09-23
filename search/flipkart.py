from bs4 import BeautifulSoup as soup
from pyquery import PyQuery as jQ
import json
from flask import url_for
import requests

def flipkart(rawquery):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]

	query=rawquery.replace(" ","-")

	try:
		
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
		f=requests.get("https://flipkart.com/search?q={}".format(query),headers=headers)

		if f.ok :
			pass
		else :
			errorimg=url_for('static',filename='images/error.png')
			imglink.append(errorimg)
			prices.append("Unavilable")
			producttitle.append("Something Went Wrong")
			productlink.append("#")





		ft=soup(f.content,'lxml')
		fk=ft.find('script',id='is_script').text

		remove1=fk.replace('window.__INITIAL_STATE__ = ','')
		remove2=remove1[:-2]
		k1=json.loads(remove2)
		
		for x in range(1,11):
			j=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['media']['images'][0]['url'])
			width=j.replace("{@width}","250")
			height=width.replace("{@height}","250")
			final=height.replace("{@quality}","70")
			imglink.append(final)
			
		
		for x in range(1,11):
			l=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['pricing']['finalPrice']['decimalValue'])
			rs="₹"+l
			prices.append(rs)
			

		for x in range(1,11):
			m=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['smartUrl'])
			productlink.append(m)
			


		for x in range(1,11):
			n=(k1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['titles']['title'])
			o=n[0:33]+"..."
			producttitle.append(o)
			

	except:
		
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")
		

	return(zip(imglink,prices,producttitle,productlink))