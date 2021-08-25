import sys
sys.stdin = open('input.txt')

def code(data):
    while True:
        for j in range(1, 6):       # 5번의 동작이 한 사이클
            x = data.pop(0)         # queue에서 첫번째 값을 꺼내서
            if x-j > 0:             # 1~5를 뺀 값이 0 보다 크면
                data.append(x-j)    # 뺀 값을 뒤로 이동
            else:                   # 1~5를 뺀 값이 0 이하면
                data.append(0)      # 뒤에 0을 저장하고
                return data         # queue를 반환

T = 10

for _ in range(1, T+1):
    test_case = int(input())
    data = list(map(int, input().split()))

    print('#{}'.format(test_case), *code(data))