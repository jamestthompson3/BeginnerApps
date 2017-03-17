import requests
import re
from re import sub
import urllib
from bs4 import BeautifulSoup
import csv
from time import time
import mechanize
import cookielib
br = mechanize.Browser()

# Cookie Jar


#set up url and bs4
#url='https://twitter.com/search?q=%23trump&src=hash'

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
see=br.open('https://login.crowdcompass.com/login/names')

# View available forms
#for f in br.forms():
   	#print f
print see.read()

# Select the second (index one) form (the first form is a search query box)
#br.select_form(nr=0)

# User credentials
#br.form['first-name'] = 'Taylor'
#br.form['last-name'] = 'Thompson'
#br.submit()
#br.form['reg-code'] = 'JGQFP6'

# Login
#br.submit()
#r=br.submit()
#r=br.open('https://app.lead411.com/index.php/cart')
#soup=BeautifulSoup(r.read(), 'lxml')
#tags=[p.text for p in soup.findAll('a')]

		
#define data
#tweets=[p.text for p in soup.findAll('p', class_="tweet-text")]
#users=[p.text for p in soup.findAll('strong', class_="fullname")]
##print(tags)

#print to csv
##with open ('attend.csv',"a") as csv_file:
		#writer=csv.writer(csv_file)
		#writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in tags])
		#writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in tweets])
		#writer.writerow(tags)
		#writer.writerow([tweets])
