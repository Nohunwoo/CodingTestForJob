def solution(str_list, ex):
    answer = ""
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

## 리스트 컴프리헨션으로도 풀 수 있다.
## def solution(str_list, ex):
## return "".join(i for i in str_list if ex not in i)
## 이게 더 빠르고 정확하다
