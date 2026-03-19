# Silver 5

n= int(input())
num_list = list(map(int, input().split()))

answer = (max(num_list)-min(num_list))*2

print(answer)