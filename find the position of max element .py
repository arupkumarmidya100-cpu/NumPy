import numpy as np

arr = np.array([12, 45, 23, 89, 34, 67])

index = np.argmax(arr)

print("Index:", index)
print("Maximum value:", arr[index])