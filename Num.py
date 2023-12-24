a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)
import math
from math import sin,pi,cos
print(sin(pi))
print(cos(pi))
import numpy as np
a =np.array([1,2,3,4,])
print(type(a))
b=np.array([[1,2,3,4],[2,5,9,1],[1,2,3,4]])
print(b)
print(len(a))
print(a[0])
print(a[::]) #4
print(b[::2,::2]) #3 row,column
print(len(a))
print(len(b))
print(a.shape)
print(b.shape)
print(a.size)
print(b.size)
b = list(range(0,10,2))
print(b)
a =np.arange(3,10)
a=np.arange(3,10.5,2.5)
print(a)
a=np.linspace(0,10,5)
a=np.zeros(5,dtype=int)
a=np.zeros((5,5))
print(a)
a=np.ones((3,4))
print(a)
print(a+1)
print(a*15216)
#boolean indexing/boolean mask/logical expression
a = np.array([1,2,9,8,3,4])
print(a>3)
b=np.array([9,8,1,2,5,6])
print(a>b) #boolean/logical expression
print(a[a>3]) #boolean indexing
a[a>3]=0
print(a) #boolean indexing
print(b>3)
a[b>3]=0
print(a)
print(b)

#Excercises
#Bai 19
import numpy as np
x = np.array([1,4,3,2,9,4])
y = np.array([2,3,4,1,2,3])
u = x + y
v = x*y
w = x/y
z = np.sin(x)
r = 8*np.sin(x)
s = 5*np.sin(x*y)
p = x**y
print(u)
print(v)
print(w)
print(z)
print(r)
print(s)
print(p)
#Bai 20
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

#Bai 1
r = np.linspace(0, 29, 9)
squared = np.square(r)
addition = r + r
multiplication = r * 2
print("Array r:\n ",r)
print("Square of each element:\n",squared)
print("Twice the value of each element :\n",addition)
print("Twice the value of each element :\n",multiplication)