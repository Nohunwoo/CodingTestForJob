word = input()
i = 0
answer = 0
while i < len(word) //2:
    if word[i] == word[len(word)-i-1]:
        answer += 1
    else:
        answer = 0
        break
    i += 1

if answer == len(word) // 2:
    print(1)
else:
    print(0)