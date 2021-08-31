# 스위치를 상태를 바꾸는 함수
def swap(a):
    if switch[a]:
        switch[a] = 0
    else:
        switch[a] = 1

N = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)

M = int(input())
student = []
for _ in range(M):
    student.append(list(map(int, input().split())))

for i in range(M):
    s, n = student[i]

    if s == 1:                              # 남학생이면
        for i in range(1, N//n+1):          # 모든 스위치 중
            swap(n*i)                       # 받은 숫자 n의 배수인 번호의 스위치 상태를 바꾼다
    elif s == 2:                            # 여학생이면
        for i in range(min(n, N-n+1)):      # 보다 가까운 가장자리까지 좌우로 탐색하며
            if switch[n-i] == switch[n+i]:  # 대칭되는 숫자가 같으면
                if i == 0:                  # 스위치의 상태를 바꾼다
                    swap(n-i)
                else:
                    swap(n-i)
                    swap(n+i)
            else:
                break

result = switch[1:]

# 20개씩 끊어서 출력
for i in range(N):
    if (i+1) % 20 == 0:
        print(result[i])
    else:
        print(result[i], end=' ')