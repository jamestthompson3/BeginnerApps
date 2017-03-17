import time
from datetime import datetime as dt
hosts_path="/private/etc/hosts"
redirect="127.0.0.1"
website_list=["https://www.facebook.com","https://www.reddit.com", "www.reddit.com"]
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
		print ("Go Back to Work!")
		with open(hosts_path, 'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write("\n"+redirect+"	"+website+"\n")
		#import localsetup.py
	else:
		with open(hosts_path, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("you good brah")
	time.sleep(5)