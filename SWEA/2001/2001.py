import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_count = 0

    for i in range(N-M+1):                      # MxM 행렬이 NxN 행렬 안을 돌아다닐 때 인덱스 i, j
        for j in range(N-M+1):
            fly_count = 0
            for fi in range(i, i+M):            # MxM 행렬 내부 인덱스 fi, fj
                for fj in range(j, j+M):
                    fly_count += arr[fi][fj]    # MxM 행렬 내부값들의 합
            if max_count < fly_count:           # 최대값 구하기
                max_count = fly_count

    print('#{0} {1}'.format(test_case, max_count))
