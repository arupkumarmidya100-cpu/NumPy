import numpy as np
arr=np.array([10,20,30,40,50])
avg=np.mean(arr)
print("Average:",avg)
print("Above average:",arr[arr>avg])