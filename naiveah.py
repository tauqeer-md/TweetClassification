# importing necessary libraries 
from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
import csv
import numpy as np


data = np.loadtxt('ddd.csv', delimiter=',')

# loading the iris dataset 

m = data.shape[1]-1
# use slicing to extract subarrays
X = data[:,:m]
y = data[:,m]

# dividing X, y into train and test data 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 

# training a Naive Bayes classifier 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB().fit(X_train, y_train) 
gnb_predictions = gnb.predict(X_test) 
##print(X_test)
##print(gnb_predictions)


# accuracy on X_test 
accuracy = gnb.score(X_test, y_test) 
print (accuracy) 

# creating a confusion matrix 
cm = confusion_matrix(y_test, gnb_predictions) 
