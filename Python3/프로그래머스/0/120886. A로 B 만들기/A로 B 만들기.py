def solution(before, after):
    answer = 0
    after = list(after)
    for i in before:
        if i in after:
            answer +=1
            after.remove(i)

    if answer == len(before):
        answer = 1
    else : answer = 0
    
    return answer