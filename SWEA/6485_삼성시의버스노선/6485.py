import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # bus dictionary = key : 정류장, value : 버스노선의 수
    bus = {}
    for i in range(1, 5001):
        bus[i] = 0
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus[j] += 1

    # result에는 Cj정류장들의 버스 노선 수 저장
    P = int(input())
    result = []
    for i in range(P):
        result.append(bus[int(input())])

    print('#{}'.format(test_case), *result)