import numpy as np
'''
1️⃣ Create a 1D NumPy array of numbers from 10 to 50.
2️⃣ Create a 2D array of shape (3, 3) filled with zeros.
3️⃣ Create a 5x5 identity matrix.
4️⃣ Create a NumPy array containing 20 linearly spaced points between 0 and 1.
5️⃣ Check the shape, size, and data type of an array.
'''
# arr  = np.arange(10,51,1)
# arr2 = np.zeros((3,3))
# arr3 = np.eye((5))
# arr4 = np.linspace(0,1,20)

# print(arr4.shape)
# print(arr4.dtype)
# print(arr4.size)
# print(arr4)
'''
6️⃣ Create a 1D array of numbers from 0 to 9, and extract elements from index 2 to 6.
7️⃣ Reshape a 1D array of 16 elements into a 4x4 matrix.
8️⃣ Reverse a NumPy array (use slicing).
9️⃣ Split a NumPy array of 10 elements into two equal parts.
🔟 Replace all odd numbers in an array with -1.
'''
# arr_num = np.arange(0,10,1)
# sub_arr_num = arr_num[2:7:1]
# print(arr_num)
# print(sub_arr_num)

# arr_num = np.arange(1,17,1)
# new_arr = np.reshape(arr_num,(4,4))
# print(arr_num)
# print(new_arr[::-1])

# arr_num = np.arange(1,11,1)
# arr_num[(arr_num & 1).astype(bool)] =-1
# print(arr_num)

'''
1️⃣1️⃣ Create two 3x3 arrays of random numbers and add them element-wise.
1️⃣2️⃣ Multiply a 2D array by a scalar value.
1️⃣3️⃣ Compute the mean, median, standard deviation, min, and max of an array.
1️⃣4️⃣ Find the position (index) of the maximum value in a 1D array.
1️⃣5️⃣ Perform element-wise modulo operation between two arrays using np.mod()
1️⃣1️⃣ Create two 3×3 arrays with random integers and perform addition.
1️⃣2️⃣ Compute the mean, standard deviation, and variance of a random array.
1️⃣3️⃣ Find the index of the maximum and minimum values in a NumPy array.
1️⃣4️⃣ Multiply a 3×3 matrix by a scalar 5.
1️⃣5️⃣ Perform element-wise modulus operation between two arrays.
'''
# arr1 = np.random.randint(0,10,(3,3))
# arr2 = np.random.randint(0,10,(3,3))

# print(arr1)
# print(arr2)
# print(arr1+arr2)

# arr1 = np.random.randint(1,10,(10,))
# print(arr1)
# print(f"mean: {np.mean(arr1)}")
# print(f"mean: {arr1.mean()}")
# print(f"median: {np.median(arr1)}")
# print(f"standard deviation: {np.std(arr1)}")
# print(f"variance: {np.var(arr1)}")


# arr1 = np.random.randint(1,10,(10,))
# print(arr1)
# max = np.argmax(arr1)
# min = np.argmin(arr1)
# print(max,arr1[max])
# print(min,arr1[min])

# arr1 = np.random.randint(1,10,(10,))
# arr2 = np.random.randint(1,10,(10,))
# print(arr1)
# print(arr2)

# mod_arr = np.mod(arr2,arr1)

# print(mod_arr)
'''
1️⃣6️⃣ Find all numbers greater than 50 in a random array of numbers between 0 and 100.
1️⃣7️⃣ Replace all negative numbers in an array with 0.
1️⃣8️⃣ Extract all numbers between 25 and 75 from an array.
1️⃣9️⃣ Count how many even numbers are there in a NumPy array.

'''
#16 arr1 = np.random.randint(0,100,(20,))
# arr2 =arr1[arr1 > 50]
# print(arr1)
# print(arr2)


#17 arr1 = np.random.randint(-20,20,(10,))
# print(arr1)
# arr1[arr1 < 0] = 0
# print(arr1)

#18 arr1 = np.random.randint(20,80,(15,))
# print(arr1)
# arr2 = arr1[(arr1 > 25) & (arr1 <75)]
# print(arr2)


#19 arr1 = np.random.randint(1,100,(20,))
# even_num = np.sum(arr1 > 20)
# print(arr1)
# print(even_num)

'''
2️⃣0️⃣ Stack two 2×3 arrays vertically and horizontally.
2️⃣1️⃣ Split a 4×4 matrix into four equal 2×2 sub-matrices.
2️⃣2️⃣ Create a checkerboard pattern (8×8 matrix of alternating 0s and 1s).
2️⃣3️⃣ Rotate a 3×3 matrix by 90 degrees clockwise.
2️⃣4️⃣ Find unique elements and their counts in a NumPy array.
2️⃣5️⃣ Normalize a NumPy array so its values fall between 0 and 1
'''
# arr1 = np.random.randint(0,10,(2,3))
# arr2 = np.random.randint(0,10,(2,3))
# arr3 = np.vstack((arr1,arr2))
# arr4 = np.hstack((arr1,arr2))
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)


arr1 = np.random.randint(0,10,(4,4))
print(arr1)
a,b,c,d = np.split(arr1,(4),axis=1)
print(a)
print(b)
print(c)
print(d)