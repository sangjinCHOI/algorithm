import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    multiply = []

    '''
    숫자열의 길이에 따라 달라지므로 길이 조건에 따라 경우를 나눔
    짧은 숫자열의 index는 고정하고, 긴 숫자열의 index를 바꿔가며 곱셈
    곱셈 후 결과인 count를 multiply 리스트에 저장
    '''
    if N < M:
        for j in range(M-N+1):
            count = 0
            for i in range(N):
                count += A[i] * B[i+j]
            multiply.append(count)
    else:
        for j in range(N-M+1):
            count = 0
            for i in range(M):
                count += A[i+j] * B[i]
            multiply.append(count)

    result = max(multiply)

    print('#{} {}'.format(test_case, result))