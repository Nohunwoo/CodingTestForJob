import sys
input = sys.stdin.readline

n = int(input())
x_y = []
for i in range(n):
    x, y = map(int, input().split())
    x_y.append([x,y])

x_y.sort()

for x, y in x_y:
    print(f'{x} {y}')