import sys
sys.stdin = open('input.txt')

# 단어와 숫자를 매치하는 dictionary 정의
number_match = dict(ZRO=0, ONE=1, TWO=2, THR=3, FOR=4, FIV=5, SIX=6, SVN=7, EGT=8, NIN=9)
reverse_dict = dict(map(reversed, number_match.items()))

T = int(input())
for _ in range(1, T+1):
    test_case, N = input().split()
    number_char = list(input().split())
    number_int = []

    # 단어를 숫자로 변환해 number_int에 저장
    for number in number_char:
        number_int.append(number_match[number])

    # number_int를 정렬해 다시 단어로 출력
    print(test_case)
    for num in sorted(number_int):
        print(reverse_dict[num], end=' ')
    print()