import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)

num_list = sorted(num_list)
for i in range(n):
    print(num_list[i])