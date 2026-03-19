def solution(s):
    alpha_list = []
    for i in s:
        if len(alpha_list) == 0: 
            alpha_list.append(i)
        elif alpha_list[-1] != i:
            alpha_list.append(i)
        else :
            alpha_list.pop()

    if len(alpha_list) == 0:
        return 1
    else:
        return 0