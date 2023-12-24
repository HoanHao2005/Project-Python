#Cau 3
def my_inside_triangle(x, y):
    v0 = (0, 0)
    v1 = (1, 0)
     v2 = (0, 1)
    
    v0p = (x - v0[0], y - v0[1])
    v1p = (x - v1[0], y - v1[1])
    v2p = (x - v2[0], y - v2[1])

    dot00 = v0p[0] * v0p[0] + v0p[1] * v0p[1]
    dot01 = v0p[0] * v1p[0] + v0p[1] * v1p[1]
    dot02 = v0p[0] * v2p[0] + v0p[1] * v2p[1]
    dot11 = v1p[0] * v1p[0] + v1p[1] * v1p[1]
    dot12 = v1p[0] * v2p[0] + v1p[1] * v2p[1]

    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    if u < 0 or v < 0 or (u + v) > 1:
        return "outside"
    elif u == 0 or v == 0 or (u + v) == 1:
        return "border"
    else:
        return "inside"

print(my_inside_triangle(-1,2))
#Cau 4
def my_make_size10(x):
    if len(x) >= 10:
        return x[:10]
    else:
        return x + [0] * (10 - len(x))

array1 = [1, 2, 3, 4]
result1 = my_make_size10(array1)
print(result1)