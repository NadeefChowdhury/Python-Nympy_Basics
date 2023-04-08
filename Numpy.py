
#import numpy
import numpy as np




#create an array of integers from 10 to 50
np.arange(10,51)





#create an array of even integers from 10 to 50
np.arange(10,51,2)





#create a 3x3 matrix of integers from 0 to 8
np.arange(9).reshape(3,3)





#create an 8x8 identity matrix
np.eye(8)





#create an array of  6 random numbers
np.random.rand(6)








#create a 5x5 matrix of  25 random numbers
np.random.randn(25).reshape(5,5)





#create a 10x10 matrix of numbers from 0.01 to 1.00
np.arange(0.01,1.01,0.01).reshape(10,10)





#create a 5x5 matrix of numbers from 1 to 25
b = np.arange(1,26).reshape(5,5)





#find the sum of the numbers in the rows
b.sum(axis=1)




