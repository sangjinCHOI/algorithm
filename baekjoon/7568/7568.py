N = int(input())
people = []
result = []

for _ in range(N):
    people.append(list(map(int, input().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end=' ')