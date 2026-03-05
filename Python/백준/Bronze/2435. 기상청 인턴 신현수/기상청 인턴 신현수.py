import sys
input = sys.stdin.readline

day, stric = map(int, input().split())
day_list = list(map(int, input().split()))
strics = []
for i in range(len(day_list)):
    if i+stric > len(day_list):
        break
    stric_sum = sum(day_list[i:i+stric])
    strics.append(stric_sum)

print(max(strics))