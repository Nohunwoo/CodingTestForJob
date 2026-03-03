import sys
input = sys.stdin.readline

list_basket =[]
basket, times = map(int, input().split())
for i in range(basket+1):
    list_basket.append(i)
for j in range(times):
    change_fir, change_sec = map(int, input().split())
    temp = list_basket[change_fir]
    list_basket[change_fir] = list_basket[change_sec]
    list_basket[change_sec] = temp
print(*list_basket[1:])