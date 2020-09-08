import scrapy
import os
from bs4 import BeautifulSoup as soup
import codecs
import json
from pyquery import PyQuery as jQ


def flipoff():
	image=[]
	url=[]
	title=[]
#-----flipkart offer shower
	flipkart= os.system("scrapy fetch --nolog https://www.flipkart.com > flipkartoffer.html")
	opener=codecs.open("flipkartoffer.html", 'r','utf-8-sig')
	read=opener.read()
	query= jQ(read)

	script=query("#is_script").text()
	remove1=script.replace('window.__INITIAL_STATE__ = ','')
	remove2=remove1[:-1]
	json1=json.loads(remove2)
# print(remove2)

	for x in range(1,8):
		k=(json1['pageDataV4']['page']['data']['10000'][0]['widget']['data']['renderableComponents'][x]['value']['primaryImage']['dynamicImageUrl'])
		width=k.replace("{@width}","250")
		height=width.replace("{@height}","250")
		final=height.replace("{@quality}","70")
		image.append(final)
		# print(final)

	for x in range(1,8):
		k=(json1['pageDataV4']['page']['data']['10000'][0]['widget']['data']['renderableComponents'][x]['value']['shareUrl'])
		url.append(k)

	for x in range(1,8):
		tit=(json1['pageDataV4']['page']['data']['10000'][0]['widget']['data']['renderableComponents'][x]['value']['name'])
		tit1=tit[0:33]+"..."
		title.append(tit1)

	return(zip(image,url,title))
