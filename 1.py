"""
31
"""

#from math import factorial

def fun():
    r = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    m = [0, 2, 5]
    res = 0
    for i in range(1, 3):
        for j in range(1, 11):
            x = j - m[i]
            if x < 0:
                continue
            if x == 0:
                r[i][j-1] = 1
            if x > 0:
                r[i][j-1] = r[0][x-1] + r[1][x-1] + r[2][x-1]

        #print(r[i])

    for i in r:
        res += i[9]
    return res



print(fun())