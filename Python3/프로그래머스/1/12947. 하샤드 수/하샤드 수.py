def solution(x):
    answer = list(str(x))
    num = 0
    for i in range(len(answer)):
        num += int(answer[i])
    if x % num == 0:
        return True
    else:
        return False