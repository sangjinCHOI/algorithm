# 백준 1436
N = int(input())
count = 1
number = 0

while count <= N:
    if str(666) in str(number):
        if count == N:
            break
        else:
            number += 1
            count += 1
    else:
        number +=1

print(number)