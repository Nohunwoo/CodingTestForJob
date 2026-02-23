n = int(input())
sen = input()
answer = ''.join(" " if i.isalpha() else i for i in sen)
answer = answer.split()
int_answer = 0
for i in answer:
    int_answer += int(i)
print(int_answer)