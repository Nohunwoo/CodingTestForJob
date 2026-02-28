n= int(input())
hash_word = input()
answer = 0
for i in range(len(hash_word)):
    answer += (ord(hash_word[i])-96) * (31**i)
print(answer)