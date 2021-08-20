import sys
sys.stdin = open('input.txt')

T = int(input())
pascal = []

for test_case in range(1, T+1):
    N = int(input())
    line = [0 for _ in range(N)]

    # N번째 줄 구하기
    for i in range(0, N):
        if i == 0:
            line[i] = 1                     # 1 첫번째 숫자는 1
        elif i == N - 1:
            line[i] = 1                     # 3-1 마지막 숫자는 1
            tmp = line[::]                  # 3-2 N+1번째 줄을 구하기 위해 tmp에 line을 저장
        else:
            line[i] = tmp[i - 1] + tmp[i]   # 2 i번째 값은 이전 줄(tmp)의 i-1 값 + i 값
    pascal.append(line)                     # 4 기존의 파스칼의 삼각형에 N번째 줄 추가

    print('#{0}'.format(test_case))
    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()