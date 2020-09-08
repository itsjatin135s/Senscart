from bs4 import BeautifulSoup as soup
from pyquery import PyQuery as jQ
import json
import codecs



imglink=[]
prices=[]
product=[]
productlink=[]

mt=codecs.open("myntra.html", 'r','utf-8-sig')
script=mt.read()

start='<script>window.__myx = '
end='</script><script>window["__myx_apps__"]'

start1='''"https://www.youtube.com/user/myntradotcom"
	            ]
	        }
	    </script>
    
		
		<script type="application/ld+json">'''
end1='</script>'

try:
	remove1=(script.split(start))[1].split(end)[0]
	json1=json.loads(remove1)


	for x in range(0,10):
		k=(json1['searchData']['results']['products'][x]['images'][1]['src'])
		imglink.append(k)


	for x in range(0,10):
		l=(json1['searchData']['results']['products'][x]['price'])
		prices.append(l)




	remove2=(script.split(start1))[1].split(end1)[0]
	json2=json.loads(remove2)



	for x in range(0,10):
		m=json2['itemListElement'][x]['name']
		product.append(m)


	for x in range(0,10):
		n=json2['itemListElement'][x]['url']
		print(n)

except:
	print("error somewhere")



# print(imglink)
# print(prices)
# print(product)
# print(productlink)
