#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
#sys.path.append("../tools/")
cwd = os.getcwd()
sys.path.append(cwd+"/git/python101/MachineLearning/tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# create a classifier
clf = GaussianNB()
#clf.fit(features_train,labels_train)  
#somelist = clf.fit_predict(X,Y)  #to try, see if it works
## X or features_train,np.array; Y or labels/classes or labels_train, np.array
##clf.predict([[x1,x2,...]])  #predict for instance, given x feature values
#pred = clf.predict(features_test)


#########################################################


