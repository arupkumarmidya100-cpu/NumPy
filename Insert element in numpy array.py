#1D ARRAY:-


import numpy as np
var=np.array([1,2,3,4,5])
x=np.insert(var,(2,4),40)
print(x)

# 2D ARRAY:-

import numpy as np
var1=np.array([[1,2,3],[4,5,7]])
y=np.insert(var1,2,[22,44,33],axis=0)
print(y)