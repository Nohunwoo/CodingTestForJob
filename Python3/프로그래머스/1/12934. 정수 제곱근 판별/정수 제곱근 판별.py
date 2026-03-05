def solution(n):
    answer = 0
    x = int(n**(1/2))
    if x**2 == n:
        answer = (x+1)**2
    else :
        answer = -1
    return answer