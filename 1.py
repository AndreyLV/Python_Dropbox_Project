"""
31
"""

#from math import factorial

def fun(x = 5, y = 0):
    global res
    global t
    t += 1
    p = [5, 2, 1]
    for n in p:
        if y > n:
            continue
        for i in range(1, 11):
            s = x + (n * i)
            if (s) > 10:
                break
            if (s) == 10:
                print("x=", x, "n=", n, "i=", i, "t", t)
                res += 1
            if (s) < 10:
                fun(s, n)
    t -= 1
    return res


res = 0
t = 0
print(fun())