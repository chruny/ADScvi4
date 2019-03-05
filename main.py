import numpy as np


def load_file():
    lines2 = []
    with open('cviko4.txt') as file:
        lines = file.readlines()
        for line in lines:
            line = [x.strip() for x in line.split(',')]
            line = list(map(int, line))
            lines2.append(line)
        print(len(lines2))
    return lines2


def load_file2():
    matrix = np.zeros((1000, 4), dtype=np.int)
    with open('cviko4.txt') as file:
        for index, line in enumerate(file):
            pole = np.asarray(line.strip().split(','))
            matrix[index] = pole
    return matrix


def knapsack(W, data, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            if data[i - 1][3] <= w and data[i - 1][1] <= w:
                K[i][w] = max(data[i - 1][0] + K[i - 1][w - data[i - 1][3]],
                              data[i - 1][2] + K[i - 1][w - data[i - 1][1]],
                              K[i - 1][w])
            elif data[i - 1][1] <= w < data[i - 1][3]:
                K[i][w] = max(data[i - 1][0] + K[i - 1][w - data[i - 1][1]], K[i - 1][w])

            elif data[i - 1][3] <= w < data[i - 1][1]:
                K[i][w] = max(data[i - 1][2] + K[i - 1][w - data[i - 1][3]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


def main():
    data = load_file()
    data2 = load_file2()
    W = 2000
    n = len(data)
    n2 = len(data2)
    print(knapsack(W, data, n))
    print(knapsack(W, data2, n2))


if __name__ == '__main__':
    main()
