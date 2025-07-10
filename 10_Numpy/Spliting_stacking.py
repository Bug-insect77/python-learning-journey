import  numpy as np
#Spliting
'''
np.split(array, indices_or_sections, axis)

It splits an array into multiple sub-arrays.

indices_or_sections:

If an integer → splits array into that many equal parts

If a list/array of indices → splits at those indices.

axis:

axis=0 → split along rows (vertical split)

axis=1 → split along columns (horizontal split)
'''
# arr1 = np.array([[1,2,3],[4,5,6]])
# # new_arr ,new_arr1 ,new_arr2 = np.split(arr1,3,axis=1)


# new_arr= np.split(arr1,2,axis=0)
# print(new_arr)
'''
arr1 has shape (2, 3) → 2 rows, 3 columns.
np.split(arr1, 2, axis=0)
splits along rows into 2 equal parts.
'''
# arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# x, y, z = np.split(arr3, [3, 6])
# print(x)  # [1 2 3]
# print(y)  # [4 5 6]
# print(z)  # [7 8 9]

#Vsplit and Hsplit
# arr4 = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]])
# arr = np.split(arr4,3,axis=0)
# print(arr[0])

#stacking : also called concatination
arr = np.array([[1,2,3,4,5],[1,1,1,1,1]])
arr2 = np.array([5,4,3,2,1])
new_arr = np.append(arr,[[4],[4]],axis=1)
print(new_arr)

'''
arr3 = np.hstack((arr,arr2))
arr4 = np.vstack((arr,arr2))
print(arr3)
print(arr4)
'''

