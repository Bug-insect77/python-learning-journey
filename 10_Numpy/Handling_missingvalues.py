#Builtin Functions
#np.isnan detect missing values
#np.nan_to_num() converting nan to number
#np.isinf() detect infinite values

import numpy as np

# arr = np.array([1,np.nan,2,3,np.nan,4,np.nan])

# print(np.isnan(arr))
# # we cant compare the nan values with each other

# # clean_arr = np.nan_to_num(arr,9)
# clean_arr = np.nan_to_num(arr,nan=10)
# print(clean_arr)

arr2 = np.array([1,np.inf,2,3,-np.inf,4,np.inf])
print(np.isinf(arr2))
clean_arr = np.nan_to_num(arr2,posinf=1000, neginf=-1000)
print(clean_arr )