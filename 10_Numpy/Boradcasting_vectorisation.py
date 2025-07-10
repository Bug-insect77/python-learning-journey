import numpy as np
# arr = np.array([100,200,300])
# my_list = [100,200,300]
# dicount = 10
# final_prices =[]
# for items in my_list:
#     final_p = items - (items * dicount/100)
#     final_prices.append(final_p)

# final_prices2 = arr - (arr * dicount/100)

# print(final_prices)
# print(final_prices2)

#Broadcasting 
'''
how numpy handle differnt shapes of  arrays
1 matching dimensions a1 = [1,2,3] a2 =[1,2,3]
then add = [2,4,6]
2 expanding single element
a1 = [1,2,3] a2 =[1]
then addition = [2,3,4]
3 Incompatible shapes                           
'''
#
'''
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,2,3,4,5])
 
result= arr1 * arr2
result2 = arr1[arr1 > 2]
print(result2)
'''
#
'''
matrix1 = np.array([[1,2],[3,4],[6,7]])
vector1 = np.array([[1,2]])

matrix2 = np.array([[1,2],[3,4],[6,7]])
vector2 = np.array([[1],[2],[3]])
 
print(matrix1 * vector1)
print(matrix2 * vector2)
'''
# something need to be match for broadcasting it can be row or column
 
