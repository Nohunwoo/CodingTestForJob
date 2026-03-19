# Silver 5
import sys
input = sys.stdin.readline

n= int(input()) # 입력받을 숫자 길이
word1 = input().strip()
word2 = input().strip()

# 두 단어의 첫글자와 마지막 글자가 동일한지 확인
cond1 = (word1[0] == word2[0]) and (word1[-1] == word2[-1])

# 한 단어를 재배열해서 다른 단어를 만들수 있는지 확인
cond2 = (sorted(word1) == sorted(word2))

# 각 단어가 aeiou를 제외하고 동일해야함
vowel = ["a","e","i","o","u"]
temp1 = word1
temp2 = word2
for i in vowel:
    temp1 = temp1.replace(i,"")
    temp2 = temp2.replace(i,"")

cond3 =  (temp1 == temp2)

if cond1 and cond2 and cond3:
    print("YES")
else:
    print("NO")