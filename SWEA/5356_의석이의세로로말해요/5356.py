import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # 5개의 단어와 최대 15의 글자 개수
    N = 5
    M = 15
    words = []
    for _ in range(N):
        words.append(' '.join(input()).split())

    print('#{}'.format(test_case), end=' ')
    for i in range(M):
        for j in range(N):
            try:
                print(words[j][i], end='')
            except(IndexError):
                pass
    print()