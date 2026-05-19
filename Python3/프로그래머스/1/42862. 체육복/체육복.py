def solution(n, lost, reserve):
    real_reserve = [x for x in reserve if x not in lost]
    real_lost = [x for x in lost if x not in reserve]
    
    real_reserve = sorted(real_reserve)
    real_lost = sorted(real_lost)
    
    answer = n - len(real_lost)
    
    for i in real_lost:
        if i - 1 in real_reserve:
            real_reserve.remove(i - 1)
            answer += 1 
            
        elif i + 1 in real_reserve:
            real_reserve.remove(i + 1)
            answer += 1 
            
    return answer