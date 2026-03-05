import sys
input = sys.stdin.readline

basket, mix = map(int, input().split())
basket_ls = []
for i in range(basket+1):
    basket_ls.append(i)
for i in range(mix):
    start, end = map(int, input().split())
    basket_ls = basket_ls[:start] + basket_ls[end:start-1:-1] +basket_ls[end+1:]
print(*basket_ls[1:])