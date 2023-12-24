#Cau 2
def operation(a, b, operation):
    if operation == "plus":
        return a + b
    elif operation == "minus":
        return a - b
    elif operation == "mult":
        return a * b
    elif operation == "div":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == "pow":
        return a ** b
    else:
        return "Error: Invalid operation"
print(operation(1,8,"plus"))

#Cau 6
def diem(percent):
    if percent > 97:
        return "A+"
    elif percent > 93:
        return "A"
    elif percent > 90:
        return "A-"
    elif percent > 87:
        return "B+"
    elif percent > 83:
        return "B"
    elif percent > 80:
        return "B-"
    elif percent > 77:
        return "C+"
    elif percent > 73:
        return "C"
    elif percent > 70:
        return "C-"
    elif percent > 67:
        return "D+"
    elif percent > 63:
        return "D"
    elif percent > 60:
        return "D-"
    else:
        return "F"
print(diem(15))
print(diem(60))
print(diem(98))

#Cau 7
def alarm(s1, s2, s3):
    if abs(s1 - s2) > 10 or abs(s1 - s3) > 10 or abs(s2 - s3) > 10:
        return "alarm!"
    else:
        return "normal"
print(alarm(50, 55, 59))

#Cau 8
import math

def my_n_roots(a, b, c):
    discriminant = b*2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return 2, [root1, root2]
    elif discriminant == 0:
        root = -b / (2*a)
        return 1, [root]
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return -2, [root1, root2]
print(my_n_roots(3,1 , 2))