import numpy as np
print(type(np.arange))
#self-defined function

print(1)
def ourprint(x,y="UEH"): #function definition
    print("Hello",x)
    print("Welcome to",y)

ourprint("An") #call function
print("Binh")
ourprint("Cuong", "3I")
ourprint("Wjbungu")
ourprint(100)

def cal(x=10,y=5,z=50): #x=10,y=20,z=30
  #print(x+y+z)
  return x*y+z*2
print("1",cal(20,30)) #x*y+z*2 = 20*30+50*2=700
print(cal()) #x*y+z*2 = 10*5+50*2=150
print("end")

def tinh(x1,y1,z1): #tinh(5,10,20) x=5,y=10,z=20
    t=x2*y1+z1*2 #90
    print("inside",x1,y1,z1,t) #5 10 20 90
    print(x2)
    return t,z1 #90 20

x2,y2,z2 = 10,20,5 #global
b,a = tinh(z2,x2,y2) #b,a = tinh(5,10,20) = 90,20
print(a,b) #20 90
print("outside",x2,y2,z2) #10 20 5
print(x2)

def tinhtoan(x):
    global n
    n=x**2
    print(n)

n= 10
print(10)
tinhtoan(5)
print(n)

#anonymous function
def square(x,y):
    print("Hello")
    return (x+y)**2

a=square(5,2)
print(a)

sq2 = lambda x,y:(x+y)**2 #1 line method
b=sq2(5)
print(b)
import numpy as np

def func(f,x):
    return f(x)+1

print(func(np.sin,np.pi/2)) #2
print(func(np.cos,np.pi/2)) #1
print(func(lambda x:x+2,2))