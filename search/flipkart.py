from bs4 import BeautifulSoup as soup
from pyquery import PyQuery as jQ
import json
import codecs
from flask import url_for


def flipkart(query):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]


	try:
		file="flipkart{}.html".format(query)
		opener=codecs.open(file, 'r','utf-8-sig')
		read=opener.read()
		query= jQ(read)


		script=query("#is_script").text()
		remove1=script.replace('window.__INITIAL_STATE__ = ','')
		remove2=remove1[:-1]
		json1=json.loads(remove2)

		for x in range(1,11):
			k=(json1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['media']['images'][0]['url'])
			width=k.replace("{@width}","250")
			height=width.replace("{@height}","250")
			final=height.replace("{@quality}","70")
			imglink.append(final)


		for x in range(1,11):
			l=(json1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['pricing']['finalPrice']['decimalValue'])
			rs="₹"+l
			prices.append(rs)


		for x in range(1,11):
			m=(json1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['smartUrl'])
			productlink.append(m)


		for x in range(1,11):
			n=(json1['pageDataV4']['page']['data']['10003'][x]['widget']['data']['products'][0]['productInfo']['value']['titles']['title'])
			o=n[0:33]+"..."
			producttitle.append(o)

	except:
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")


	return(zip(imglink,prices,producttitle,productlink))

# print(imglink)
# print(prices)
# print(product)
# print(productlink)



