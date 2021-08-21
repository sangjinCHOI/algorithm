import sys
sys.stdin = open('input.txt')

# 배열을 시계방향으로 90도 회전시키는 함수
def rotate(arr):
    N = len(arr)
    rot = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rot[i][j] = arr[(N-1) - j][i]

    return rot

# 출력을 위해 배열의 행을 하나의 string으로 묶는 함수
def out(arr):
    N = len(arr)
    tmp = []

    for i in range(N):
        char = ''
        for j in range(N):
            char += str(arr[i][j])
        tmp.append(char)

    return tmp

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    print('#{}'.format(test_case))
    for i in range(N):
        print('{} {} {}'.format(out(arr_90)[i], out(arr_180)[i], out(arr_270)[i]))