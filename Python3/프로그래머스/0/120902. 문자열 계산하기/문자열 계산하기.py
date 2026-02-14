def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1,len(s),2):
        ope = s[i]
        number = int(s[i+1])
        if ope == '+' :
            answer += number
        elif ope == '-' :
            answer -= number
    return answer

#1. 문자열로 된 a+b 또는 a-b 수식 입력받음
#2. a와 b 분리, +또는 - 분리
#3. a,b를 숫자로 바꿔서 더하기 또는 빼기 작업 진행
#4. 결과값 출력