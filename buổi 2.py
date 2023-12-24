p = 1
q = 2
x = (not(p and q))==((not p) or (not q))
y = ( not(p and q)) == ((not p) and (not q))

p = False
q = True
x = (p and (not q))
print(x)

#import math
#a = math.exp(2)*math.sin(math.pi/6)+math.log(3)*math.cos(math.pi/9)-5**3
#print(a)



