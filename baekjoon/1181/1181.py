N = int(input())
words = []
for _ in range(N):
    words.append(input())
# 중복제거를 위해 set으로 변환 후, 다시 list로 변환
words = list(set(words))

# 첫번째는 길이, 두번째는 알파벳 순서로 정렬
words.sort(key=lambda x: [len(x), x])

for word in words:
    print(word)