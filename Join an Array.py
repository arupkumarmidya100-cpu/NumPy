# 1D ARRAY:

import numpy as np
var=np.array([1,2,3,4])
var1=np.array([9,8,7,6])
ar=np.concatenate ((var,var1))
print(ar)
print()
print()

# 2D ARRAY :

var2=np.array([[1,2],[3,4]])
var3=np.array([[9,8],[7,6]])
ar_new=np.concatenate((var2,var3),axis=1)
print(ar_new)