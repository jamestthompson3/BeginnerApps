import re
from numpy import *
from sklearn.feature_extraction.text import TfidfTransformer as tfidf
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.naive_bayes import GaussianNB as gnb
import pandas as pd
def parse(bigstring):
	tokenlist=re.split(r'\W*', bigstring)
	return [tok.lower() for tok in tokenlist if len(tok) >3][:8]
#vect=bagofwords2vec(myvocab, listposts[3])
df=pd.read_csv("tweettest.csv", delimiter=',')
oppose=pd.read_csv("opppose.csv", delimiter=',', encoding='latin-1')
supp=pd.read_csv("support.csv", delimiter=',', encoding='latin-1')
cleansupp=supp.dropna()
supset=cleansupp.to_string()
cleanop=oppose.dropna()
opposet=cleanop.to_string()
clean=df.dropna()
st=clean.to_string()
def supporttest2():
	doclist=[]; classlist=[]; fulltext=[]
	for i in range (1, 26):
		wordlist=parse(opposet)
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(0)
		wordlist=parse(supset)
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(1)
	return doclist, classlist
features_train, labels_train=supporttest2()
def testset():
	doclist=[]
	for i in range (1, 26):
		wordlist=parse(supset)
		doclist.append(wordlist)
	return doclist
xtrain=map(''.join, features_train)
ltrain=asarray(labels_train)
features_test=testset()
vecorizer=cv()
xt=vecorizer.fit_transform(xtrain).toarray()
tester=map(''.join, features_test)
x_test=vecorizer.fit_transform(tester).toarray()
clf=gnb()
clf.fit(xt, ltrain)
pred=clf.predict(x_test)8
print pred

