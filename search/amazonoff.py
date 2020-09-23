import requests
from bs4 import BeautifulSoup as soup



def amzoff():
	photo=[]
	productink=[]
	title=[]
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
	amazons = requests.get("https://www.amazon.in/",headers=headers)
	soup1=soup(amazons.text,'lxml')



	limit=0
	j=soup1.find_all('img',{'class':'product-image'})
	for image in j:
		if limit<6:
			limit=limit+1
			photo.append(image['src'])
			tit=image['title'][0:33]+"..."
			title.append(tit)

		else:
			break

	limit1=0
	j=soup1.find_all('div',{'class':'deals-shoveler-card-image'})
	for image in j:
		k=image.find_all('a')
		if limit1<6:
			for image1 in k:
				limit1=limit1+1
				productink.append("https://amazon.in"+image1['href'])
		else:
			break
	return(zip(photo,productink,title))