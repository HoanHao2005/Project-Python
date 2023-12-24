#Bai 2
import numpy as np
def my_checker_board(n):
    m=np.zeros((5,5),dtype=int)
    m[::2,::2]=m[1::2,1::2]=1
    return m
print(my_checker_board(1))
#Bai 4
def my_split_matrix(m):
    columns = len(m[0])
    middle = columns // 2

    m1 = [row[:middle] for row in m]
    m2 = [row[middle:] for row in m]

    return [m1, m2]

matrix1 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

result1 = my_split_matrix(matrix1)
print(result1)

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

result2 = my_split_matrix(matrix2)
print(result2)

matrix3 = [[1, 2],
           [3, 4],
           [5, 6],
           [7, 8]]

result3 = my_split_matrix(matrix3)
print(result3)

#Bai 6
import numpy as np

def my_n_odds(a):
    count = 0

    for num in a:
        if num % 2 != 0:
            count += 1

    return count

# Test Cases
arr1 = np.arange(100)
print(my_n_odds(arr1))  # Output: 50

arr2 = np.arange(2, 100, 2)
print(my_n_odds(arr2))  # Output: 0
#Bai 7
def my_twos(m, n):
    return np.full((m, n), 2)
print(my_twos(1, 4))
#Bai 13
def dungsaichophep(A, a, dungsai):
    B = []

    for num in A:
        if abs(num - a) < dungsai:
            B.append(num)

    return B

# Hàm main để thực hiện ví dụ
def main():
    A = [0, 1, 2, 3, 4, 5]
    a = 2
    dungsai = 1.5

    B = dungsaichophep(A, a, dungsai)
    print("Kết quả:", B)

if __name__ == '__main__':
    main()


