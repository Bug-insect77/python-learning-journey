import numpy as np

'''
numpy_array_2d = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,9]])

print(numpy_array_2d)
print(f"Shape: {numpy_array_2d.shape}") #Gives shape
print(f"Data type: {numpy_array_2d.dtype}") #Data type
print(f"Dimension: {numpy_array_2d.ndim}")  #Number of dimensions
'''
#Type conversion of array 
'''
arr = np.array([1,2.9,3,4,5])
print(arr.dtype)
new_arr =  arr.astype(int)
print(new_arr.dtype)

'''
#Mathematical operation in numpy arrays
'''
arr = np.array([[2,4,6,8,10],[1,3,5,7,9]])
print(arr+10)
print(arr-10)
print(arr*10)
print(arr ** 2) 
'''

#Aggregation functions np.min() ,np.mean()
# arr = np.array([10,20,30,40,50])
# print("Minimum value: ",np.min(arr))
# print("Maximum value: ",np.max(arr))
# print("Mean value: ",np.mean(arr))
# print("Median value: ",np.median(arr))
# print("Sum : ",np.sum(arr))
# print("Standard Deviation: ",np.std(arr))
# print("Variance: ",np.var(arr))


