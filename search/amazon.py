from urllib.request import urlopen
#above is only for amazon because of 503 response
from bs4 import BeautifulSoup as soup
import requests
from flask import url_for


def amazon(rawquery):

	imglink=[]
	prices=[]
	producttitle=[]
	productlink=[]


	query=rawquery.replace(" ","-")
	try:
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
		amazons = requests.get("https://www.amazon.in/s?k={}".format(query),headers=headers,verify=False)
		# amazons=urlopen('https://amazon.in/s?k=iphone').read()
		soup1=soup(amazons.text,'lxml')
		

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

	except :
		errorimg=url_for('static',filename='images/error.png')
		imglink.append(errorimg)
		prices.append("Unavilable")
		producttitle.append("Something Went Wrong")
		productlink.append("#")


	return(zip(imglink,prices,producttitle,productlink))