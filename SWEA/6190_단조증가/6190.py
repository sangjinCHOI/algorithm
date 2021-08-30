import sys
sys.stdin = open('input.txt')

# 단조증가인지 판단하는 함수
def increase_num(num):              # 각자리 숫자를 비교하므로 num은 string 형태
    for k in range(1, len(num)):    # 첫번째 숫자부터 마지막 숫자까지
        if num[k-1] > num[k]:       # k-1번째 숫자가 k번째 숫자보다 크면
            return 0                # 단조증가 수가 아니므로 0을 반환
    return 1                        # 단조증가 수이면 1을 반환

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split())) 
    multiply = []

    # 숫자들의 곱이 단조증가이면 multiply 리스트에 저장
    for i in range(N-1):
        for j in range(1, N-i):
            x = A[i] * A[i + j]
            if increase_num(str(x)):
                multiply.append(x)

    # multiply 리스트의 최대값을 결과값으로 저장
    # multiply 리스트가 비어있다면 결과값으로 -1
    if multiply:
        result = max(multiply)
    else:
        result = -1

    print('#{} {}'.format(test_case, result))

