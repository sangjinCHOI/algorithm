import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    test_case = input()
    word = input()
    sentence = input()

    # 반복문, index, 결과를 위한 값 정의
    M = len(word)
    N = len(sentence)
    i = 0
    j = 0
    count = 0

    # Brute Force
    while j <= M and i < N:
        if sentence[i] != word[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == M:      # 모든 글자가 일치했을때
            count += 1  # count를 1증가시키고
            j = 0       # 단어의 index를 0으로 초기화

    print('#{0} {1}'.format(test_case, count))



