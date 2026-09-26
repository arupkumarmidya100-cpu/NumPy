# 1D ARRAY:-

import numpy as np
var=np.array([1,2,3,5,4,7,8,2,6,2])
x=np.where(var==2)
print(x)
print()

# 2D ARRAY :-

var1=np.array([[1,2,3,4],[9,0,8,2],[2,4,5,7]])
print(var1)
x1=np.where(var1==2)
print(x1)
print()

# 3D ARRAY:-

var2=np.array([[[1,2,3],[3,4,5],[9,8,3],[5,6,3]]])
print(var2)
x2=np.where (var2==3)
print(x2)


# FOR SORTED ARRAY :-
import numpy as np
var3=np.array([1,2,3,4,5,7,8,9])
x3=np.searchsorted(var3,6,side="right")
print(x3)