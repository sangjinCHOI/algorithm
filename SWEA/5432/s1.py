import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 괄호가 많기 때문에 Lazer를 의미하는 ()는 L로 대체
    bar = input().replace('()', 'L')
    i = 0
    count = 0	# 쇠막대기의 수
    result = 0	# 잘려나온 조각의 수

    while i < len(bar):
        if bar[i] == 'L':           # L이 나타날 때(레이저 쏘기)
            result += count         # 쇠막대기 수만큼 조각갯수 증가
            i += 1                  # 다음칸으로
            
        elif bar[i] == '(':         # (가 나타날 때
            count += 1              # 쇠막대기 1개 추가
            i += 1                  # 다음칸으로
            
        else:                       # )가 나타날 때
            count -= 1              # 쇠막대기 1개 감소
            result += 1             # 조각갯수 1개 증가(마지막 자투리)
            i += 1                  # 다음칸으로

    print('#{0} {1}'.format(test_case, result))