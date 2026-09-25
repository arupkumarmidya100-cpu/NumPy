# 1D ARRAY:-
import numpy as np
var=np.array([1,2,3,4,5,6,7,8])
ar=np.array_split(var,3)
print(ar)
print(ar[0])
print()

# 2D ARRAY:-

import numpy as np
var1=np.array([[1,2,3,4],[9,8,7,6]])
print(var1)
ar_new=np.array_split(var1,5,axis=0)
print(ar_new)