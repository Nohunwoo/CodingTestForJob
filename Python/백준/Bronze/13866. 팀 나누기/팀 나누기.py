a,b,c,d = map(int, input().split())
list = [a,b,c,d]

first = max(list) + min(list)
second = sum(list) - first
answer = abs(first - second)
print(answer)