# 균형잡인 문자열인지 판단하는 함수 balance 정의
def balance(sentence):
    for char in sentence:
        # 여는 괄호면 stack에 추가
        if char == '[' or char == '(':
            stack.append(char)
        # 닫는 대괄호일때
        elif char == ']':
            if len(stack) == 0:
                return 'no'
            else:
                x = stack.pop()
                if x != '[':
                    return 'no'
        # 닫는 소괄호일때
        elif char == ')':
            if len(stack) == 0:
                return 'no'
            else:
                x = stack.pop()
                if x != '(':
                    return 'no'
        # 문장이 종료되면 반복문 종료
        elif char == '.':
            break

    # stack에 무언가 남으면 균형을 이루지 않음
    if stack:
        return 'no'
    # stack이 비었으면 균형을 이룸
    else:
        return 'yes'


while True:
    sentence = list(map(str, input()))
    stack = []

    # 입력의 종료조건인 .을 만족하면 반복문 종료
    if sentence == ['.']:
        break
    # 종료조건이 아닌경우 결과 출력
    else:
        result = balance(sentence)
        print(result)