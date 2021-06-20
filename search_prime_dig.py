""" Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом? """

from math import sqrt


def prost():
    result = [2, 3, 5, 7, 11, 13]
    dig = 14
    while len(result) < 10001:
        prvsimv = str(dig)[len(str(dig))-1]
        if (prvsimv == '1') or (prvsimv == '3') or (prvsimv == '7') or (prvsimv == '9'):
            for i in range(3, int(sqrt(dig)+1)):
                if dig % i == 0:
                    break
                if i == int(sqrt(dig)):
                    result.append(dig)
        dig += 1
    return result


z = prost()
print(len(z))
print(z[10000])