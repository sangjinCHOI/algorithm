import sys
sys.stdin = open('input.txt')

# 회문의 갯수를 구하는 함수
def palindrome(M, array) :
    N = len(array)
    count_row = 0
    count_col = 0

    # 가로방향의 회문의 갯수 구하기
    for i in range(N):
        for j in range(N-M+1):
            tmp_row = ''
            for nj in range(j, j+M):
                tmp_row += array[i][nj]
            if tmp_row == tmp_row[::-1]:
                count_row += 1

    # 세로방향의 회문의 갯수 구하기
    for j in range(N):
        for i in range(N-M+1):
            tmp_col = ''
            for ni in range(i, i+M):
                tmp_col += array[ni][j]
            if tmp_col == tmp_col[::-1]:
                count_col += 1

    return count_row + count_col


T = 10

for test_case in range(1, T+1):
    length = int(input())

    board = [[0] * 8 for _ in range(8)]
    for row in range(8):
        tmp = input()
        for col in range(8):
            board[row][col] = tmp[col]

    result = palindrome(length, board)
    print('#{0} {1}'.format(test_case, result))