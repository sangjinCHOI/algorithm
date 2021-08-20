import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case, N = list(map(int, input().split()))
    road = list(map(int, input().split()))

    # i번째 index에는 i에서 출발해 도착할 수 있는 노드를 저장
    path = [[] for _ in range(100)]
    for i in range(N):
        path[road[2*i]].append(road[2*i+1])

    visited = [0] * 100
    stack = [0]
    result = 0

    # DFS로 탐색
    while len(stack):
        current = stack.pop()

        # 도착점에 도착했을때
        if current == 99:
            result = 1
            break

        # 현재 위치가 이미 방문했을때 / 방문하지 않았을때
        if visited[current] == 1:
            continue
        else:
            visited[current] = 1

        # stack에 다음 위치 저장
        for w in path[current]:
            if visited[w] == 0:
                stack.append(w)

    print('#{} {}'.format(test_case, result))