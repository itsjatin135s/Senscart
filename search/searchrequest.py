#imports
import scrapy
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

	#search request to all the websites--------------------------------------------------------------------------------------------
	flipkart= os.system("scrapy fetch --nolog https://www.flipkart.com/search?q={} > flipkart{}.html".format(query,query))
	# myntra=os.system("scrapy fetch --nolog https://www.myntra.com/{} > myntra.html".format(query))
	amazon=os.system("scrapy fetch --nolog https://www.amazon.in/s?k={} > amazon{}.html".format(query,query))
	snapdeal=os.system("scrapy fetch --nolog https://www.snapdeal.com/search?keyword={} > snapdeal{}.html".format(query,query))
	# print("task success searched for" + x)
	return query