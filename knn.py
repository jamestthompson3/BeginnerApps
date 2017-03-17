from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier as randfo
import operator
from numpy import zeros
def file2matrix(filename):
    love_dictionary={'largeDoses':3, 'smallDoses':2, 'didntLike':1}
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)            #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if(listFromLine[-1].isdigit()):
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
datingdata, datinglabels = file2matrix("datingTestSet.txt")
testdata, testlabels =file2matrix("datingTestSet2.txt")

def classifyPerson():
	percentTats=float(raw_input('percentage of time spent playing games'))
	ffmiles=float(raw_input('frequent flier miles'))
	icream=float(raw_input('liters of ice cream'))
	inarr=[ffmiles, percentTats, icream]
	return inarr
#clf=knn(n_neighbors=2)
#clf.fit(datingdata,datinglabels)
inputs=classifyPerson()
#pred=clf.predict(inputs)

clf=randfo(n_estimators=10)
clf.fit(datingdata, datinglabels)
pred=clf.predict(inputs)
acc=accuracy_score(pred,testlabels[:1])
print acc