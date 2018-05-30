from random import choice 
from numpy import array, dot, random
from pylab import plot, ylim 

#Creating a step function 
stepfunction = lambda x: 0 if x < 0 else 1

#inputting training data 
training_data = [ (array([-0.1,0.0]), 0), 
				  (array([0.0,9.0]), 0),
				  (array([10.0,0.0]), 1), 
				  (array([10.0,8.0]), 1), 
]

#Altered weight due to incorrect output of second array 
w = random.rand(2) - ([0.0,9.0])

#Error values 
errors = [] 
#Variable controlling learning rate 
eta = 0.2
#Number of iterations 
n = 100

#Calculating the Dot Product to act like a function 
for i in xrange(n): 
	x, expected = choice(training_data) 
	result = dot(w, x) 
	error = expected - stepfunction(result) 
	errors.append(error) 
	w += eta * x

#Printing results 
for x, _ in training_data: 
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:2], result, stepfunction(result)))



