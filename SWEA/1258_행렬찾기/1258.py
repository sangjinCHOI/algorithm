import sys
sys.stdin = open('input.txt')

# 사각형의 왼쪽상단을 찾는 함수
def find_point(arr):
    global x, y
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                x, y = i, j
                return

# 사각형의 크기를 구하는 함수
def find_size(arr):
    global col, row
    for j in range(y, N):
        if arr[x][j] == 0 or j == N-1:
            col = j - y
            break
    for i in range(x, N):
        if arr[i][y] == 0 or i == N-1:
            row = i - x
            break
    result.append([row, col])
    return

# 이미 구한 사각형을 0으로 변환하는 함수
def zero(arr):
    for i in range(x, x+row):
        for j in range(y, y+col):
            arr[i][j] = 0
    return arr

# 사각형을 구하는 함수
def find_square(arr):
    find_point(arr)
    find_size(arr)
    zero(arr)
    return arr


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = [[0] * N for _ in range(N)]
    result = []

    # 사각형을 모두 구할때까지 반복
    while arr != tmp:
        find_square(arr)

    # 사각형의 크기, 행 순으로 정렬
    result.sort(key=lambda x: [x[0]*x[1], x[0]])

    # 출력하기
    print('#{} {}'.format(test_case, len(result)), end=' ')
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j], end=' ')
    print()