import numpy as np
def splitm(m):
col = m.shape[1] #lay phan tu thu nhat cua m
#col=len(m[0])
print(m[:,:(col+1)//2])
print(m[:,(col+1)//2:])
m = np.array([[0,1,2,3,4,5],[2,4,6,8,10,1],[1,3,5,7,9,1]])
splitm(m)
m=np.array([[0,1,2,3],[2,4,6,8],[1,3,5,7]])
splitm(m)
m=np.array([[0,1,2],[2,4,6],[1,3,5]])
splitm(m)
