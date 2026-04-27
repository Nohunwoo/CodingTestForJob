def solution(n):
    three = []
    ten = 0
    while n > 0 :
        w = n % 3
        three.append(w)
        n = n // 3
    for i in range(len(three)):
        ten += three[len(three)-i-1]*(3**i)
    return ten