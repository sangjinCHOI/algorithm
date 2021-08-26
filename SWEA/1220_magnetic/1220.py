import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        col = []
        for j in range(N):
            if table[j][i]:                     # table의 i번째 열에서
                col.append(table[j][i])         # 값이 0이 아닌 1,2 만 col에 저장

        for k in range(len(col)-1):             # col의 범위 내에서
            if col[k] == 1 and col[k+1] == 2:   # 1,2가 연달아 나올 때(=교착일 때)
                count += 1                      # count를 1증가

    print('#{} {}'.format(test_case, count))