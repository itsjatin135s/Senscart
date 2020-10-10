from urllib.request import urlopen
#above is only for amazon because of 503 response
from bs4 import BeautifulSoup as soup
import requests
from flask import url_for
import random

def amazon(rawquery):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]


	query=rawquery.replace(" ","-")
	# try:
	# proxies={'https':'103.61.100.49:34144'}


	# agent=['Mozilla/5.0 (Amiga; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
	# 		'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15',
	# 		'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
	# 		'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.1) Gecko/20061220 BonEcho/2.0.0.1',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.10) Gecko/20071128 BonEcho/2.0.0.10',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.17) Gecko/20080831 BonEcho/2.0.0.17',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.6) Gecko/20070731 BonEcho/2.0.0.6',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.7) Gecko/20070917 BonEcho/2.0.0.7',
	# 		'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1b2) Gecko/200609']
	# x=random.randint(0,9)

	a=[]
	f=open('useragent.txt','r')
	for i in f:
		a.append(i)
	agent=a[random.randint(0,998)].replace('\n','')
	
	headers = {'User-Agent':agent}
	amazons = requests.get("https://www.amazon.in/s?k={}".format(query),headers=headers,verify=False)
	# amazons=urlopen('https://amazon.in/s?k=iphone').read()
	soup1=soup(amazons.text,'lxml')
	print(soup1)

	# if amazons.ok:
	# 	pass
	# else :
	# 	amazons = requests.get("https://www.amazon.in/s?k={}".format(query),headers=headers)
	# 	soup1=soup(amazons.text,'lxml')

	# 	if amazons.ok :
	# 		pass
	# 	else:
	# 		errorimg=url_for('static',filename='images/error.png')
	# 		imglink.append(errorimg)
	# 		prices.append("Unavilable")
	# 		producttitle.append("Something Went Wrong")
	# 		productlink.append("#")
	


	limit=0
	divs = soup1.find_all('div',{'class':'a-section aok-relative s-image-fixed-height'})
	for mdivs in divs:
		j=mdivs.find_all('img',{'class':'s-image'})
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
	divsk = soup1.find_all('div',{'class':'a-row'})
	for mdivsk in divsk:
		k=mdivsk.find_all('span',{'class':'a-price-whole'})
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

	# except :
	# 	errorimg=url_for('static',filename='images/error.png')
	# 	imglink.append(errorimg)
	# 	prices.append("Unavilable")
	# 	producttitle.append("Something Went Wrong")
	# 	productlink.append("#")


	return(zip(imglink,prices,producttitle,productlink))