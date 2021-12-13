import math
import random
from matplotlib import pyplot as plt

def suma(x, w):
    s = 0
    for j in range(len(x)):
        s += w[j] * x[j]
    s += w[2] * 1
    return s

def f_out(s):
    return 1 / (1 + math.exp(- (1 * s)))

def f_out_dx(s):
    return math.exp(- (1 * s)) / ((1 + math.exp(- (1 * s))) ** 2)

def eps(t, out):
    return 0.5 * (out - t)**2

def delta(t, out, s):
    return (out - t) * f_out_dx(s)

def main():
    arr_x = [[0, 0],
             [1, 0],
             [0, 1],
             [1, 1]]

    arr_y = [0, 0, 0, 1]

    arr_w = [random.random(), random.random(), random.random()]
    loss = []
    counter = 0

    notCorrect = True

    while notCorrect:
        notCorrect = False
        counter += 1
        e = 0
        for k in range(len(arr_x)):
            s = suma(arr_x[k], arr_w)
            out = f_out(s)
            e = eps(arr_y[k], out)
            if e <= 0.001:
                continue
            notCorrect = True

            d = delta(arr_y[k], out, s)
            n = 0.6

            arr_w[0] -= n * d * arr_x[k][0]
            arr_w[1] -= n * d * arr_x[k][1]
            arr_w[2] -= n * d
        
        loss.append(e)
    k = - (arr_w[1] / arr_w[0])
    b = - (arr_w[2] / arr_w[0])

    x1 = -0.5
    x2 = 1.5

    plt.plot([x1, x2], [x1 * k + b, x2 * k + b])

    for x in arr_x:
        plt.plot(x[0], x[1], "ro")

    print("Number of generations - " + str(counter))
    print(arr_w)

    for k in range(len(arr_x)):
        print('[' + str(arr_x[k][0]) + ', ' + str(arr_x[k][1])  + '] -> ' + str(f_out(suma(arr_x[k], arr_w))))

    plt.grid()
    plt.show()

    plt.plot(loss)
    plt.show()


main()
