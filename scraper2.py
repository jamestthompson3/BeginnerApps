import requests
from re import sub
from bs4 import BeautifulSoup
import csv
import numpy as np
import time
#set up url and bs4
#url='https://twitter.com/search?q=trump&src=hash'
i=0
while i < 40:
	def scraperbot(url):
		r=requests.get(url)
		soup=BeautifulSoup(r.content, 'html.parser')
		everything=soup.findAll('p', class_='tweet-text')
		for tweet in everything:
			print tweet.text
		
		
	tags=scraperbot('https://twitter.com/search?f=tweets&vertical=news&q=%23trump&src=hash')
	#users=[p.text for p in soup.findAll('strong', class_="fullname")]
	#print(tags)
	#print to csv
	#with open ('tweettest.csv',"a") as csv_file:
		#writer=csv.writer(csv_file)
		#writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in tuptag])
		#writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in tweets])
		#writer.writerow(tags)
		#writer.writerow([tweets])
	time.sleep(60)
	i +=1