n = int(input())
x_y = []
for i in range(n):
    x, y = map(int, input().split())
    x_y.append([x,y])

x_y = sorted(x_y)

for i in range(len(x_y)):
    print(f'{x_y[i][0]} {x_y[i][1]}')