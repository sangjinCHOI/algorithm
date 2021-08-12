import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = list(list(map(int, input().split())) for _ in range(N))
    result = 0

    # 가로 확인
    for i in range(N):
        row_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_count += 1              # row_count에 연속된 1의 갯수를 저장
            if arr[i][j] == 0 or j == N-1:  # 값이 0이거나 마지막 숫자일 때
                if row_count == K:          # row_count 값이 k라면
                    result += 1             # 결과값 1 추가
                row_count = 0

    # 세로 확인
    for i in range(N):
        col_count = 0
        for j in range(N):
            if arr[j][i] == 1:              # i, j 인덱스 순서를 바꿔 세로 파악
                col_count += 1              # col_count에 연속된 1의 갯수를 저장
            if arr[j][i] == 0 or j == N-1:  # 값이 0이거나 마지막 숫자일 때
                if col_count == K:          # col_count 값이 k라면
                    result += 1             # 결과값 1 추가
                col_count = 0

    print('#{0} {1}'.format(test_case, result))


