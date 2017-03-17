import csv
from sklearn.naive_bayes import GaussianNB
from numpy import *

def loadDataSet():
	postinglist=[['trump', 'stupid', 'racist', 'resist'],['great', 'maga', 'america', 'cops','love'],['fake', 'alternative','ban', 'muslim', 'stupid'], ['praise', 'support', 'build' 'wall'], ['fucking', 'idiot', 'doomed', 'protest']]
	classVec=[1,0,1,0,1]
	return postinglist, classVec
def createVocabList(dataset):
	vocabSet = set([])
	for document in dataset:
		vocabSet=vocabSet | set(document)
	return list(vocabSet)
#def setofWords2Vec(vocabList, inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else: print "the word: %s is not in my Vocabulary!" % word
	return returnVec
#def trainNB0(trainMatrix,trainCategory):
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)
	p0Num = zeros(numWords); p1Num = zeros(numWords)
	p0Denom = 0.0; p1Denom = 0.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 1:
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
#def bagOfWords2VecMN(vocablist, inputset):
	returnVec = [0]*len(vocablist)
	for word in inputset:
		if word in vocablist:
			returnVec[vocablist.index(word)] +=1
	return returnVec
#def classifyNB(vec2classify, p0vec, p1vec, pclass1):
	p1=sum(vec2classify*p1vec) + log(pclass1)
	p0=sum(vec2classify*p0vec) + log(1.0-pclass1)
	if p1 > p0:
		return 1
	else:
		return 0
#def testingNB():
	listoposts,listclasses=loadDataSet()
	myvocablist=createVocabList(listoposts)
	trainmat=[]
	for postindoc in listoposts:
		trainmat.append(setofWords2Vec(myvocablist, postindoc))
		p0v,p1v,pab=trainNB0(array(trainmat), array(listclasses))
		testEntry=[open("tweet2.txt")]
		thisdoc=array(bagOfWords2VecMN(myvocablist, testEntry))
		print testEntry, 'classified as:', classifyNB(thisdoc, p0v,p1v,pab)