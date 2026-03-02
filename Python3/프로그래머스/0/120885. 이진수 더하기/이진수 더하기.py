def solution(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    answer = ''
    bin1 = bin1.rjust(max_len, '0')
    bin2 = bin2.rjust(max_len, '0')
    ndzr = 0

    for i in range(max_len-1,-1,-1):
        ndup = int(bin1[i]) + int(bin2[i]) + ndzr
        if ndup == 2 :
            ndup = 0
            ndzr = 1
        elif ndup == 3:
            ndup = 1
            ndzr = 1
        else :
            ndzr = 0
        answer += str(ndup)
        if i == 0 and ndzr == 1:
            answer += '1'
    reversed_answer = answer[::-1]
    return reversed_answer