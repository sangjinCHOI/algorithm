import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    A, B = list(input().split())
    N = len(A)
    M = len(B)
    i = 0
    j = 0
    count = 0

    # Brute Force
    while i < N and j < M:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == M:      # 모든 글자가 일치했을때
            count += 1  # count 1 증가
            j = 0       # B의 index를 0으로 초기화

    result = len(A) - ((len(B)-1) * count)
    print('#{0} {1}'.format(test_case, result))