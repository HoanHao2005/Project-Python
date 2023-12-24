def func(f,x):
    return f(x)+1
import numpy as np
print(func(np.sin,np.pi/2)) #2
print(func(np.cos,np.pi/2)) #1
print(func(lambda x:x+2,2))

#Bai 7
def my_twos(m, n):
    return np.full((m, n), 2)
print(my_twos(1, 4))

#Bai 6
import numpy as np

def my_n_odds(a):
    count = 0

    for num in a:
        if num % 2 != 0:
            count += 1

    return count
arr1 = np.arange(100)
print(my_n_odds(arr1))

arr2 = np.arange(2, 100, 2)
print(my_n_odds(arr2))