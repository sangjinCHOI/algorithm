import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 숫자가 쌓이는 방향을 따라 우,하,좌,상 순으로 di, dj 정의
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0           # di, dj 값을 바꿀 변수
    i, j = 0, -1    # 첫번째 이전값인 arr[0][-1]을 위한 i, j 정의
    count = 1       # 배열에 넣을 숫자 count 정의

    while count <= N ** 2:
        # 새로운 좌표를 위한 ni, nj 정의
        ni = i + di[k]
        nj = j + dj[k]
        if ni in range(N) and nj in range(N) and arr[ni][nj] == 0: # ni가 범위안, nj가 범위안, 배열에 숫자가 없을 때
            arr[ni][nj] = count # 숫자입력
            i, j = ni, nj       # i, j에 새로운 좌표를 대입
            count += 1          # 배열에 넣을 숫자 count를 늘림
        else:
            k = (k + 1) % 4     # 방향이 4가지 방향이므로 k = 0, 1, 2, 3중 하나가 되야함

    # 출력하기
    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()