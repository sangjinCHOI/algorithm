import sys
sys.stdin = open('input.txt')

# 우선순위를 나타내는 함수
def isp(x):
    if x == '+':
        return 1
    elif x == '*':
        return 2
    elif x == '(':
        return 0

def icp(x):
    if x == '+':
        return 1
    elif x == '*':
        return 2
    elif x == '(':
        return 3

T = 10
for test_case in range(1, T+1):
    N = int(input())
    infix = list(map(str, input()))
    postfix = []
    stack = []

    # infix to postfix
    for char in infix:
        if char.isdigit():                                          # 입력값이 숫자라면
            postfix.append(int(char))                                 # postfix에 바로 추가
        else:
            if char == '+' or char == '*':                          # 입력값이 연산자라면
                if len(stack) == 0:                                   # 스택이 비었다면
                    stack.append(char)                                  # 연산자를 stack에 push
                else:                                                 # 스택이 비어져있지 않다면
                    while len(stack) > 0:                               # 스택이 빌때까지
                        if icp(char) < isp(stack[-1]):                  # 입력값이 stack 마지막값보다 priority가 작다면
                            postfix.append(stack.pop())                 # stack의 연산자를 pop하여 postfix에 계속해서 추가
                        else:                                           # 그렇지 않다면
                            break                                       # 반복문을 나가고
                    stack.append(char)                                  # 입력값을 stack에 push
            elif char == '(':                                       # 입력값이 여는 괄호라면
                stack.append(char)                                    # stack에 바로 push
            elif char == ')':                                       # 입력값이 닫는 괄호라면
                top = stack[-1]
                while top != '(':                                     # stack의 pop할 값이 '(' 일때까지
                    postfix.append(stack.pop())                       # stack의 연산자를 pop하여 postfix에 계속해서 추가
                    top = stack[-1]
                stack.pop()                                           # '('가 나왔으면 pop하여 버림

    for _ in range(len(stack)):                                     # stack에 남은 연산자는 pop하여 postfix에 추가
        postfix.append(stack.pop())

    # 계산하기
    for char in postfix:
        if char == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif char == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(x*y)
        else:
            stack.append(int(char))
    result = stack[0]

    # 출력하기
    print('#{} {}'.format(test_case, result))