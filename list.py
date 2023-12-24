
#Bai 15:
A=(2,3,2,3,1,2,5)
B=set(A)
print(B)
#Bai 16:
set_a={2,3,2}
set_b={1,2,3}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
#Bai 17,18:
letters = {
    "A": "a",
    "B": "b",
    "C": "c"
}
print(letters)
if "B" in letters:
    print("B is in letters")
else:
    print("B is not in letters")