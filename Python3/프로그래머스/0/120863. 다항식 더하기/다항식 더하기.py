def solution(polynomial):
    num_sum = 0
    x_sum = 0
    poly_split = polynomial.split(' + ')
    for i in poly_split:
        if 'x' in i:
            if i == 'x':
                x_sum +=1
            else :
                i = i.replace('x', '')
                x_sum += int(i)
        else :
            num_sum += int(i)
    answer = []
    if x_sum > 0:
        answer.append('x' if x_sum == 1 else f'{x_sum}x')
    if num_sum > 0:
        answer.append(str(num_sum))
        
    return ' + '.join(answer)
