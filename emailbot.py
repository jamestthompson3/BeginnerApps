from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urlparse import *
from collections import deque
import re
#create url queue
new_urls=deque(['https://www.unilever.com'])
#create a set to store crawled urls
processed_urls=set()
#keep collection of emails
emails=set()
while len(new_urls):
	url=new_urls.popleft()
	processed_urls.add(url)
# extract base url and path to resolve relative links
parts=urlsplit(url)
base_url="{0.scheme}://{0.netloc}".format(parts)
path=url[:url.rfind('/')+1] if '/' in parts.path else url
#get url content
print("processing %s" % url)
try:
	response=requests.get(url)
except (requests.exceptions.MissingSchema, 
	requests.exceptions.ConnectionError):
	pass
# extract all email addresses and add them into the resulting set
new_emails=set(re.findall(r"a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", requests.get(url).text, re.I))
emails.update(new_emails)
# create a beautiful soup for the html doc
soup=BeautifulSoup(response.text)
# find and process all the anchors in the document
for anchor in soup.find_all('a'):
	link=anchor.attrs["href"] if "href" in anchor.attrs else ''
if link.startswith('/'):
	link=base_url + link
elif not link.startswith('http'):
	link=path + link
# add the new url to queue if was not processed yet
if not link in new_urls and not link in processed_urls:
	new_urls.append(link)
print emails