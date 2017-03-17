import urllib,re
f = urllib.urlopen("https://www.unileverusa.com/news/media-contacts/")
s = f.read()
number=re.findall(r"\+\d{2}\s?0?\d{10}",s)
email=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
print email
print number
