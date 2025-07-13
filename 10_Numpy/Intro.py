#NumPy (Numerical Python) is a popular Python library for numerical and scientific computations
import numpy as np
'''
#linear array
numpy_array = np.array([1,2,3,4,5,6])
print(numpy_array)
'''

'''
#2 dimensional array
# print(numpy_array_2d)
#print(numpy_array_2d.shape) #Gives shape
numpy_array_2d = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,9]])
print(numpy_array_2d.dtype) #Data type
print(numpy_array_2d.ndim)  #Number of dimensions
'''

#Some array methods 
# np.zero(shape) = np.zero((2,3))
# arrar = np.zeros((3,4))
# arrar2 = np.ones((3,4))
# arr2 = np.eye(3) # create a identity matrice
# print(arrar)
# print(arrar2)
# print(arr2)
# arr = np.full((4,4),9)
# print(arr)
# array = np.arange(2,11,2)
# print(array)
# array=np.linspace(0,5,10)
# print(array) 

'''
np.zeros((2,3)) → 2x3 array with all zeros

np.ones((3,4)) → 3x4 array with all ones

np.full((2,2), 7) → 2x2 array filled with 7

np.eye(3) → 3x3 identity matrix. Only take one argument

np.arange(0, 10, 2) → Return an array of numbers from 0 to 8 with step of 2

np.linspace(0, 5, 10) → 10 evenly spaced values from 0 to 5
[0.   0.55555556 1.11111111 1.66666667 2.22222222 2.77777778 3.33333333 3.88888889 4.44444444 5.]

'''