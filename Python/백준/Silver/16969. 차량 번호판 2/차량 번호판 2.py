import sys
input = sys.stdin.readline

type = input().strip()
MOD = 1000000009
# 문제 푸는 방향성 -> type에서 dcdd같은 문자가 나올 경우
# 10 * 26 * ((10*10) - 10)이 나온다
# 연속되는 문자의 경우 따로 제곱후 d의 경우 10, c의 경우 26을 빼고 곱하면 된다
# c가 n개라면 26*(25**(n-1)) 
answer = 1

for i in range(len(type)):
    if i == 0 :
        if type[i] == 'c':
            answer *= 26
        else:
            answer *= 10
    else :
        if type[i] == 'c':
            if type[i] == type[i-1]:
                answer *= 25
            else :
                answer *= 26
        elif type[i] == 'd':
            if type[i] == type[i-1]:
                answer *= 9
            else :
                answer *= 10
    answer %= MOD

print(answer)