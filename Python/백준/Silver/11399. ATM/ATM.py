n= int(input())
atm_list = list(map(int, input().split()))

atm_list.sort()
minute = 0
answer = 0
# atm 리스트에 3 1 4 3 2를 정렬
for i in atm_list:
    # 임시 변수 minute에 숫자를 누적 저장
    minute += i
    # 정답은 1+ (1+2) + (1+2+3) 누적 방식
    answer += minute
    
print(answer)