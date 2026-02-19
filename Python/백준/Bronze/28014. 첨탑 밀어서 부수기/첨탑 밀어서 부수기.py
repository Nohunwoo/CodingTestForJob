n = int(input())
top = list(map(int, input().split()))
answer = 1
for i in range(1,n):
    if top[i-1] <= top[i] :
        answer +=1
print(answer)