def solution(array):
    answer = 0
    count = [0] *(max(array)+1)
    
    for i in array:
        count[i] += 1
    
    answer = max(count)
    
    if count.count(answer) >1:
        return -1
    else :
        return count.index(answer)