import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # 2개의 방이 같은 선상에서 출발하므로 200개의 방으로 범위설정
    room = [0 for _ in range(201)]

    for i in range(N):
        point = list(map(int, input().split()))
        '''
         숫자가 작은곳을 시작점, 큰곳을 도착점으로 설정하고
         1,2 / 3,4 / ... 식으로 같은 선상의 방 2개를 하나로
        '''
        start = (min(point) +1) // 2
        end = (max(point) + 1) // 2

        for j in range(start, end + 1):
            room[j] += 1

    print('#{} {}'.format(test_case, max(room)))