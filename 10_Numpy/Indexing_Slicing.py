import numpy as np
'''
arr = np.array([[10,20,30],[30,40,50]])
new_arr = arr.flatten()
print("flatten array: ",new_arr)

new_arr2 = arr.ravel()
new_arr2[0]=100 
print("new  ravel array: ",new_arr2)
print("Original array: ",arr)
'''

arr = np.array([10,20,30,40,10,40,50,60])
print(arr[0])
print(arr[1:5:1])

#boolean masking filtering
# arr[arr !=10] -=10
# print(arr)
# print(arr[arr>10])
# print(arr)

#fancy indexing
# print(arr[[1,3,5,7]])
'''
aee = arr[::-1]
arr2 = arr[2:7:1]
print(arr2)
print(aee)
'''
# a =np.array([[1,2],[3,4]])
# b =np.array([[5,6]])
# c = np.concatenate((a,b),axis=0)# axis=none then it will be a linear array
# print(c)

# a =np.array([[1,2]])
# b =np.array([[5,6]])
# c = np.concatenate((a,b),axis=1)
# print(c)

#Inserting data in np arrays 
# arr = np.array([[1,2],[3,4],[4,4]])
# # print(np.insert(arr,(2),[0,0],axis=1))
# # print(arr)

# print(arr)
# print(arr.reshape((2,3)))
# print(arr)