C='CON CAK PYTHON'
print(len(C[1:2]+C[3:4]))

A = [[1, 2, 3], [4, 5, 6]]
x = A[1][2]
print(x)




A=[[1,2,3],[4,5,6]]
A.pop(0)
print(A)
def F(a,b=0):
  tong=0
  for x in a:
    if x==0: tong=1
    else: tong = tong + x**b
  return tong
print(F([1,2,3]))
a = "Hello, World!"
print(len(a))
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[-5:-2])
c = "Con cho Dung no bip t"
print(c[-6:-3])

a = "Hello"
b = "World"
c = a +" " + b
print(c)
d= 123
e= "thang ngu"
print(str(d)+" "+e)
fruits = ['apple', 'banana', 'cherry']

fruits.remove( "cherry")

print(fruits)

thangloz = ['Dung','Thinh','Son']

thangloz.sort()

print(thangloz)
thangngu={"Dung":100,"Thinh":10,"Son":120}
print(thangngu["Thinh"])

import numpy as np
a= np.linspace(-10,10,100)
print(a)
#Bai 21
array_a=np.array([-1,0,1,2,0,3])
print(array_a[array_a>0])

#Bai 23
import numpy as np
arr = np.zeros((2, 4), dtype=int)
print(arr)

#Bai 24
import numpy as np
arr = np.zeros((2,4))
new_column = np.array([1])
arr[:, 1] = new_column
print(arr)




