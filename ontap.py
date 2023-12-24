#Cau 1
kt = "y"
while kt=="y":
  n = 0
  while n<=0:
    n=int(input("Nhap n:"))
  b = []
  for i in range(n):
    a = int(input(f"Nhap so thu {i+1}"))
    if a%2==0 : b.append(a)
  if len(b)>0 : print("So chan lon nhat la:".max(b))
  else: print("ko co so chan")
  kt = input("Nhan y de tiep tuc:")

#Cau 2
str1 = "AAAAA BBBbbbbbb. CCCCC DEF def. cccc-aaa"
str2 = str1.replace(".","")
str2 = str2. replace("_","")
str2 = str2. replace(" ", "")
str2 = str2.lower()
print(str2)
str3 = set (str2)
print (str3)
a = list(str3)
a. sort()
print(a)
for i in a:
  print ("chu cai",i, "xuat hien",str2.count(i),"lan")
