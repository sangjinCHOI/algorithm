import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = []    # 100x100 배열
    total = []  # 가로합, 세로합, 대각선합을 담을 list
    tmp = 0     # 합을 임시저장할 변수

    # 배열 가져오기
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    #가로합
    for i in range(len(arr)):
        total.append(sum(arr[i]))

    #세로합
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            tmp += arr[i][j]
        total.append(tmp)
        tmp = 0

    #우하향 대각선 합
    for i in range(len(arr)):
        tmp += arr[i][i]
    total.append(tmp)
    tmp = 0

    #좌하향 대각선 합
    for i in range(len(arr)):
        tmp += arr[i][99-i]
    total.append(tmp)
    tmp = 0

    result = max(total)

    print('#{0} {1}'.format(test_case, result))