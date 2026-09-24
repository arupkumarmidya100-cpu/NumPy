import numpy as np
var1=np.array([1,2,3,4])
var2=np.array([9,8,7,6])
arr_new=np.stack((var1,var2),axis=1)
print(arr_new)
print()
arr_new1=np.hstack((var1,var2))  #add rows
print(arr_new1)
print()
arr_new2=np.vstack((var1,var2))  #add columns
print(arr_new2)
print()
arr_new3=np.dstack((var1,var2))  #add hight
print(arr_new3)
print()