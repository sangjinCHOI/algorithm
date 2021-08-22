import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = price[-1]                   # 역으로 탐색하기 위해 마지막을 최대값으로 지정
    profit = 0

    # 뒤에서 앞으로 탐색
    for i in range(N-2, -1, -1):
        if max_price > price[i]:            # price가 최대값보다 작으면
            profit += max_price - price[i]  # 가격차이만큼 profit에 더하기
        else:                               # price가 최대값보다 크면
            max_price = price[i]            # 최대값을 변경

    print('#{} {}'.format(test_case, profit))