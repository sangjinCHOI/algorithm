# 백준 2775
num = int(input())
for _ in range(num):
    k = int(input())
    n = int(input())

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for i in range(k):
        for j in range(14):
            if j == 0:
                list[j] = 1
            else:
                list[j] = list[j-1] + list[j]

    print(list[n-1])