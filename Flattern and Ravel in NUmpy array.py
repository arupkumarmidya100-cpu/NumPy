#Flattern a numpy array:

import numpy as np
var=np.array([[1,2],[3,4]])
print(var.flatten(order="C"))

#Ravel a numpy array:-

import numpy as np
var1=np.array([[1,2],[3,4]])
print(np.ravel(var1,order="F"))