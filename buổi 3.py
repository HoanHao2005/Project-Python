a = [0,"abc",2.5,3+3j,"eee",[9,7]]
b = [0,1,2,3,4,5,6,7,8,9,]
print(type(a))
print(len(a))
print(type(a[2]))
print(b[1::2])
#a[start:stop:step]
a[0] +=5
print(a)
c=[0,2,5,6]
b=[1,9,"a",7]
print(b*2)
print(list(range(0,10,1)))
a=[0,2,2,"b",2,5,5,"a",6,5,5,"a"]
a.index(5) #tìm vị trí
a.append(1)
print(a+[3,3,3])