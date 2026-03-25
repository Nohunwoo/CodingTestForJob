c, b = map(int, input().split())

answer = c / b
if int(answer) == answer:
    print(int(answer))
else:
    print(answer)