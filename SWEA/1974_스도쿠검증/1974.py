import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = 9                                   # 스도쿠의 크기는 9로 일정
    sdoku = []                              # 스도쿠를 저장할 리스트
    cert = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # 스택 검증을 위한 리스트
    result = 1
    for _ in range(N):
        sdoku.append(list(map(int, input().split())))

    # 가로줄 검증
    for i in range(N):
        stack = [0 for _ in range(N+1)]
        for j in range(N):
            tmp = sdoku[i][j]
            stack[tmp] += 1

        if stack == cert:
            result = result and 1
        else:
            result = result and 0

    # 세로줄 검증
    for i in range(N):
        stack = [0 for _ in range(N + 1)]
        for j in range(N):
            tmp = sdoku[j][i]
            stack[tmp] += 1

        if stack == cert:
            result = result and 1
        else:
            result = result and 0

    # 3x3 검증
    for x in range(0, N, 3):
        for y in range(0, N, 3):
            stack = [0 for _ in range(N + 1)]
            for i in range(x, x+3):
                for j in range(y, y+3):
                    tmp = sdoku[i][j]
                    stack[tmp] += 1

            if stack == cert:
                result = result and 1
            else:
                result = result and 0


    print('#{} {}'.format(test_case, result))