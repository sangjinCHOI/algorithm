import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    harvest = []

    M = N//2

    # 첫번째 행에서 중간 이전까지
    for i in range(M):
        harvest.append(farm[i][M-i:M+i+1])
    # 중간 행부터 마지막까지
    for i in range(M, N):
        harvest.append(farm[i][i-M:N+M-i])

    profit = 0
    for i in range(N):
        profit += sum(harvest[i])

    print('#{} {}'.format(test_case, profit))