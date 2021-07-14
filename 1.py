"""
31
"""

#from math import factorial

def fun():
    tot = 200
    r =  [[1] * tot,
          [0] * tot,
          [0] * tot,
          [0] * tot,
          [0] * tot,
          [0] * tot,
          [0] * tot,
          [0] * tot]
    m = [1, 2, 5, 10, 20, 50, 100, 200]
    l = len(m)
    res = 0
    for i in range(1, l):
        for j in range(1, tot+1):
            x = j - m[i]
            if x < 0:
                continue
            if x == 0:
                r[i][j-1] = 1
            if x > 0:
                for n in range(l):
                    r[i][j-1] += r[n][x-1]
        #print(r[i])

    for i in r:
        res += i[tot-1]

    return res



print(fun())