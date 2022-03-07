import numpy as np

A = np.array([[2, 3, 4], # 3x3 행렬 A 생성
              [4, 8, 2],
              [1, 2, 1]])
              
print(A[1])              
print(A[:,2])              

print(A.T)
print(np.transpose(A))
#A = 대칭행렬?
