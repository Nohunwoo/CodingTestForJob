def solution(clothes):
    hash_dict = {}
    answer = 1
    for i,j in clothes:
        if j in hash_dict:
            hash_dict[j] +=1
        else:
            hash_dict[j] = 1
    print(hash_dict)
    for i in hash_dict:
        answer *= (hash_dict[i]+1)
    return answer-1