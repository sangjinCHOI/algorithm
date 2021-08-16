N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(input()))

# 체스판, 비교판, 결과값 정의
chess_w = [[0] * M for _ in range(N)]
chess_b = [[0] * M for _ in range(N)]
compare_w = [[0] * M for _ in range(N)]
compare_b = [[0] * M for _ in range(N)]
result = 64

# 왼쪽모서리가 white or black인 체스판
for i in range(N):
    for j in range(M):
        if (i+j) % 2:
            chess_w[i][j] = 'B'
            chess_b[i][j] = 'W'
        else:
            chess_w[i][j] = 'W'
            chess_b[i][j] = 'B'

# 입력값과 체스판을 비교한 0,1로 이루어진 비교판
for i in range(N):
    for j in range(M):
        if board[i][j] != chess_w[i][j]:
            compare_w[i][j] = 1
        if board[i][j] != chess_b[i][j]:
            compare_b[i][j] = 1

# 비교판을 8by8로 자르면서 작은숫자를 result에 저장
for n in range(N-8+1):
    for m in range(M-8+1):
        count_w = 0
        count_b = 0
        for row in range(n, n+8):
            for col in range(m, m+8):
                count_w += compare_w[row][col]
                count_b += compare_b[row][col]
        if result > min(count_w, count_b):
            result = min(count_w, count_b)

# 결과값 출력
print(result)