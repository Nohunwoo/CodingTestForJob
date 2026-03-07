import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 1
if n >= m :
    answer = 0
else :
    for i in range(1,n+1):
        answer = (answer * i) % m

print(answer)