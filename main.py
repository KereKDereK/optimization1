import math as mt
import numpy as np
import matplotlib.pyplot as plt


def fib(n):
    sqrt5 = mt.sqrt(5)
    fi = (sqrt5 + 1) / 2
    return int(fi ** n / sqrt5 + 0.5)


fibo_rec = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


def f(x: float):
    return np.sinh(2 * x) * np.sinh(2 * x)


def dyhotomy(a: float, b: float, eps: float, delta: float):
    counter = 0
    al = a
    bl = b
    while abs(bl - al) > 2 * delta:
        # l = bl - al
        x1 = (al + bl - eps) / 2
        x2 = (al + bl + eps) / 2
        if f(x1) > f(x2):
            al = x1
        else:
            bl = x2
        counter += 2
    res = (bl + al) / 2
    return np.array([counter, al, bl, res])


def golden_ratio(a: float, b: float, delta: float):
    counter = 0
    al = a
    bl = b
    l = bl - al
    x2 = al + (l / 1.618)
    x1 = bl - (l / 1.618)
    y1 = f(x1)
    y2 = f(x2)
    counter += 2
    while abs(bl - al) > delta:
        if y1 > y2:
            al = x1
            x1 = x2
            x2 = al + ((bl - al) / 1.618)
            y1 = y2
            y2 = f(x2)
        else:
            bl = x2
            x2 = x1
            x1 = bl - ((bl - al) / 1.618)
            y2 = y1
            y1 = f(x1)
        counter += 1
    res = (bl + al) / 2
    return np.array([counter, al, bl, res])


def fibo(a: float, b: float, n: int):
    counter = 0
    al = a
    bl = b
    x2 = al + ((bl - al) * ((fibo_rec(n - 1)) / fibo_rec(n)))
    x1 = al + ((bl - al) * ((fibo_rec(n - 2)) / fibo_rec(n)))
    y1 = f(x1)
    y2 = f(x2)
    counter += 2
    while n != 1:
        print(bl-al)
        n -= 1
        if y1 > y2:
            al = x1
            x1 = x2
            x2 = bl - (x1 - al)
            y1 = y2
            y2 = f(x2)
        else:
            bl = x2
            x2 = x1
            x1 = al + (bl - x2)
            y2 = y1
            y1 = f(x1)
        counter += 1
    res = (al + bl) / 2
    return np.array([counter, al, bl, res])


if __name__ == '__main__':

    result_d = dyhotomy(-1, 2, 0.0001, 0.001)
    x = np.linspace(-1, 2, 200)
    print(f'Кол-во операций: {result_d[0]} \n')
    print(f'Границы минимума: ({result_d[1]} ; {result_d[2]}) \n')
    print(f'Предполагаемый минимум: {result_d[3]} \n')
    plt.plot(x, f(x))
    plt.show()

    result_d = golden_ratio(-1, 2, 0.001)
    print(f'Кол-во операций: {result_d[0]} \n')
    print(f'Границы минимума: ({result_d[1]} ; {result_d[2]}) \n')
    print(f'Предполагаемый минимум: {result_d[3]} \n')

    result_d = fibo(-1, 2, 15)
    print(f'Кол-во операций: {result_d[0]} \n')
    print(f'Границы минимума: ({result_d[1]} ; {result_d[2]}) \n')
    print(f'Предполагаемый минимум: {result_d[3]} \n')
