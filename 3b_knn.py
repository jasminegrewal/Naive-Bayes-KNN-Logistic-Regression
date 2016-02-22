import csv
import math
import operator

#function to calculate the distance between two points(set1 and set2)
def calcdistance(set1, set2, length):
	distance = 0
	for x in range(length):
		distance += pow((set1[x] - set2[x]), 2)
		#length tells till which point in the set1 and set2 array are to be used to calculate distance
	return math.sqrt(distance)

#this function is used to take the k nearest neighbors from the training data based on the distance calucalted
#between sample data given and teh training data
def neighbors(givendata, sample, k):
	distances = []                 #to store distance of each data point in training data from sample point
	length = len(sample)
	for x in range(len(givendata)):
		dist = calcdistance(sample, givendata[x], length)
		distances.append((givendata[x], dist))
	print '\n'.join(map(str,distances))
	distances.sort(key=operator.itemgetter(1)) #sort the distances to find k nearest neighbors
	#print distances
	nearestneighbors = []
	for x in range(k):
		nearestneighbors.append(distances[x][0])
	return nearestneighbors

#using the k nearest neighbors from above function, this function will predict the likely output for sample point
def predict(neighbors):
	labels = {}            #to store class labels
	for x in range(len(neighbors)):
		label = neighbors[x][-1]              
		print label
		if label in labels:
			labels[label] += 1
		else:
			labels[label] = 1
	prediction = sorted(labels.iteritems(), key=operator.itemgetter(1), reverse=True) #sort in descending order
	print prediction
	return prediction[0][0] #our prediction is the first element of this array because this class is supported by more
                      #number of data points in the nearest neighbors array

def main():
    #givendata=[]       #data is read from csv file and stored into this array after converting the string values into float
    with open('data.csv','rb') as csvfile:
        indata=csv.reader(csvfile)
        trdata=list(indata)
        for x in range(len(trdata)):
            for y in range(3):
                if y == 3:
                    if trdata[x][y] == 'M':
                        trdata[x][y] = 1
                    else:
                        trdata [x][y] = 2
                trdata[x][y]=float(trdata[x][y])
            trdata.append(trdata[x])
    
    k=input('enter number of predictions to use')        #number of nearest neighbors to find
    testSet= input('enter data to be predicted')         #give the sample point to find prediction for

    kNearneighbors=neighbors(trdata,testSet,k)
    result=predict(kNearneighbors)
    print 'nearest neibhbors are'
    print kNearneighbors
    print'Prediction for gender with given data is'
    if result == 1:
        print 'M'
    else:
        print 'w'

main()
    
#Reference: http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/




    
