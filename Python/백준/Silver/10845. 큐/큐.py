# Silver 4
import sys
input = sys.stdin.readline
from collections import deque
n= int(input())

que_list = deque()
for i in range(n):
    que = input().strip().split()
    op = que[0]

    if op == 'push':
        que_list.append(int(que[1]))
    elif op == 'pop': 
        if not que_list :
            print(-1)
        else :
            print(que_list.popleft())
    elif op == 'size':
        print(len(que_list))
    if op == 'empty':
        if not que_list : print(1)
        else : print(0)
    if op == 'front':
        if not que_list: print(-1)
        else : print(que_list[0])
    if op == 'back':
        if not que_list: print(-1)
        else : print(que_list[-1])