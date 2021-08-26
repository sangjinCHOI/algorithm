import sys
sys.stdin = open('input.txt')

def route(x, y):
    global result
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        nx = x + dx[k]                          # 다음 x좌표 nx
        ny = y + dy[k]                          # 다음 y좌표 ny
        if nx in range(N) and ny in range(N):   # 다음 좌표가 미로안의 범위일 때
            if maze[nx][ny] == 3:               # 도착점에 도착하면
                result = 1                      # 결과값을 1로 바꾸고
                return result                   # 결과값 반환
            elif maze[nx][ny] == 0:             # 아직 가지 않은 길이라면
                maze[nx][ny] = 1                # 1로 값을 바꿔 다시 가지 않게끔하고
                route(nx, ny)                   # 다음 좌표를 기준으로 재귀 실행

T = 10
for _ in range(1, T+1):
    test_case = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(16)]

    result = 0
    route(1, 1)
    print("#{} {}".format(test_case, result))