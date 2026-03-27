n = int(input())
stack = []
answer = []     
count = 1
can_count = True

for i in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        answer.append('+')
        count +=1

    if stack[-1] == num:        
        stack.pop()
        answer.append('-')

    else :
        can_count = False
        break

if can_count == True:
    for i in answer:
        print(i)
else:
    print("NO")