import requests
from bs4 import BeautifulSoup as soup
import json
from pyquery import PyQuery as jQ


def flipoff():
	image=[]
	url=[]
	title=[]
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
	f=requests.get("https://flipkart.com/",headers=headers)
	ft=soup(f.content,'lxml')
	fk=ft.find('script',id='is_script').text

	remove1=fk.replace('window.__INITIAL_STATE__ = ','')
	remove2=remove1[:-2]
	json1=json.loads(remove2)


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
