grade = 9
HK = "Tot"
if grade >=8 and HK=="Tot": #and or not
    print("scholarship")
    print("congrat")
elif grade >=6.5:
    print("good")
elif grade >=5:
    print("pass")
else:
    print("ngu nhu thang bin gay")

a,b,c=10,50,30
if a>b:
    if a>c:
        max1 = a
    else:
        max1 = c
else:
    if b>c:
        max1 = b
    else:
        max1 = c
print(max1)

a,b,c=10,50,30
max2 = a
if max2<b:
    max2=b
if max2<c:max2=c
print(max2)

a,b,c,d=10,5,3,20
max3=a
if max3<b : max3=b
if max3<c : max3=c
if max3<d : max3=d
print(max3)

#a=int(input("Enter a:"))
#print(a)
#print(type(a))

a=eval(input("Enter a:"))
print(a)
print(type(a))

#conditional expression/ternary operator
grade = 7
print("excel") if grade>=8 else print("good") if grade>=6.5 else print("average") if grade>=5 else print("fail")
