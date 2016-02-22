import csv
import random
import math

def divide(data):
        label = {}
        N=len(data)
        for i in range(len(data)):
                element = data[i]
                if (element[-1] not in label):
                        label[element[-1]] = []
                label[element[-1]].append(element)
        return label
 
def mean(numbers):
        return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
        avg = mean(numbers)
        variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
        return math.sqrt(variance)

def calcparams(data):
        params = [(mean(feature), stdev(feature)) for feature in zip(*data)]
        del params[-1]
        return params
    
def divbylabel(data):
        clss = divide(data)
        params = {}
        for clsslabel, instances in clss.iteritems():
                params[clsslabel] = calcparams(instances)
        return params

def calcProb(x, mean, stdev):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calcClssProb(parameters, sample):
        probs = {}
        for clsslabel,params  in parameters.iteritems():
                probs[clsslabel] = 1
                for i in range(len(params)):
                        mean, stdev = params[i]
                        x = sample[i]
                        pd=calcProb(x,mean,stdev)
                        print 'prob densities'
                        print pd
                        probs[clsslabel] *=pd        
                        #probs[clsslabel] *= calcProb(x, mean, stdev)
                        #print probs[clsslabel]                
        print 'ClssProbabilities(x/c)'
        print probs
        return probs

def predict(parameters, sample):
        probabilities = calcClssProb(parameters, sample)
        bestLabel, bestProb = None, -1
        for clsslabel, probability in probabilities.iteritems():
                if bestLabel is None or probability > bestProb:
                        bestProb = probability
                        bestLabel = clsslabel
        return bestLabel

def getPredictions(parameters, testSet):
    result = predict(parameters, testSet)
    return result

def main():
    givendata=[]
    with open('data.csv','rb') as csvfile:
        indata=csv.reader(csvfile)
        trdata=list(indata)
        for x in range(len(trdata)):
            for y in range(4):
                #print trdata[x][y]
                if y == 3:
                    if trdata[x][y] == 'M':
                        trdata[x][y] = 1
                    else:
                        trdata [x][y] = 2
                trdata[x][y]=float(trdata[x][y])
            givendata.append(trdata[x])

    #separated=separateByClass(trainingSet)
    #print('Separated instances: {0}').format(separated)

    parameters=divbylabel(givendata)
    print('Summary by class value: {0}').format(parameters)

    testSet= input('enter data for prediction')
    prediction=getPredictions(parameters,testSet)
    if prediction == 1:
            print 'M'
    else:
            print 'W'  

main()
    
#Reference: http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
