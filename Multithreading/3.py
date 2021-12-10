import numpy as np
A = [[1,2,3],[4,5,6]]
print(A)
type(A)
A = np.asarray(A)
print(A)
type(A)

print("Maximum element is ",np.max(A))
print(np.min(A))
print(np.mean(A))
print(np.median(A))
print(np.std(A))

B = np.transpose(A)
print(B)
C = np.reshape(A,(1,6))
print(C)
rows = np.shape(C)[0]
columns = np.shape(C)[1]

print(A)
print(A[:,0])
print(A[:, 1])
print(A[:,2])
print(np.sum(A[:,0]))
print(np.sum(A[0,:]))

print("number of rows = ",rows)
print("number of columns = ", columns)
print(A[0])
print(A[:,0])
print(A[0,:])
