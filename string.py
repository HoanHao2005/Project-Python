#print("hello")
a = "xin chao" # a is a string
print(a)
print(type(a))
''''''
a = "Hello World.\n22222"
s = "administrationsadlnashakshflashsfaskmlnc  ankdhskhsklasjsajaksl"
print(s[1])
print(s[2]) #index
print(len(s)) # length
print(s[0:5]) #slicing
print(s[2:]) #ignore the end number => slide to the end
print(s[:8]) #ignore the start number => slide from the start
print (s[len(s)+5:])
print(s[len(s)-6:])
print(s[-8])
print(s[-4:5])

#check a string
m = ' He said that "O.K"'
print(m)
print('t' in m)
print('a' in m)
print('He' not in m)
c = "Hello"
d = "UEH"
print(c, d)
e = "123"
f= 123
print(e + str(f))
print(int(e)+f)
s = " Hello ABBAAB World"
print(s.count('World'))
print(s.replace('A',"1000"))
print(s.lower())
print(s.upper())
n = " mdasjhdhsadkhlkklaskldhaishhaf123s"
print(n.islower())
print(n.isupper())
print(n.isnumeric()) #number
a = " Hi, my name's UEH"
print(a.split('m')) #it seperates the string to words (based on the ' ')
