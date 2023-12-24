#Bai 1
import numpy as np
r = np.linspace(0, 29, 9)
squared = np.square(r)
addition = r + r
multiplication = r * 2
print("Array r:\n ",r)
print("Square of each element:\n",squared)
print("Twice the value of each element :\n",addition)
print("Twice the value of each element :\n",multiplication)
#Bai 2
import numpy as np
b = np.arange(0,361)
b = np.linspace(0,360,361)

c = np.linspace(0,2*np.pi,361)
#c = np.arange(0,2*np.pi+0.001,np.pi/180)
print(c-b*np.pi/180)
print(c)

#a = np.array([[1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]]) #locak
a = np.ones((8,8) ,dtype=int)
a[1:-1,1:-1] = 0
print(a)
#cau c
import numpy as np
c = np.arange(2,50,5)
c[c%3!= 0] *= -1
print(c)
#cau b
b = np.zeros((8,8),dtype = int)
b[: :2,: :2] = b[1::2,1::2] = 1
print(b)

