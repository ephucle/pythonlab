# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
dataset.shape
#dataset(768, 9)

# split into input (X) and output (y) variables
X = dataset[:,0:8]
X.shape
#X (768, 8)

#
y = dataset[:,8]
y.shape
#(768,)