#imports
import requests
import os
from spellchecker import SpellChecker

def request1(x):
	#input product name
	# x=str(input(":enter product name: "))
	#spell correction
	spell = SpellChecker() 
	# find those words that may be misspelled 
	misspelled = spell.correction(x)
	query=misspelled.replace(" ","-")
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
	#search request to all the websites--------------------------------------------------------------------------------------------
	flipkart = requests.get("https://www.flipkart.com/search?q={}".format(query),headers=headers)
	# myntra=os.system("scrapy fetch --nolog https://www.myntra.com/{} > myntra.html".format(query))
	amazon = requests.get("https://www.amazon.in/s?k={}".format(query),headers=headers)
	snapdeal = requests.get("https://www.snapdeal.com/search?keyword={}".format(query),headers=headers)
	# print("task success searched for" + x)
	return query