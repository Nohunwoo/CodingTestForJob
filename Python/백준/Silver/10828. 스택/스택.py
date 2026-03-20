# Silver 4
import sys
input = sys.stdin.readline
n = int(input())

stack_list = []
for _ in range(n):
    stack = input().strip().split()
    # push X: 정수 X를 스택에 넣는 연산이다.
    if stack[0] == 'push':
        stack_list.append(int(stack[1]))
    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif stack[0] == 'pop':
        if stack_list:
            print(stack_list[-1])
            stack_list.pop()
        elif not stack_list :
                print(-1)
    # size: 스택에 들어있는 정수의 개수를 출력한다.
    elif stack[0] == 'size':
        print(len(stack_list))
    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif stack[0] == 'empty':
        if not stack_list :
            print(1)
        else : print(0)
    # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
    elif stack[0] == 'top':
        if not stack_list :
            print(-1)
        else:
            print(stack_list[-1])