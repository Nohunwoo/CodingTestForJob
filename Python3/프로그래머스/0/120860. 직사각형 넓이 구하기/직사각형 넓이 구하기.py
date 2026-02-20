def solution(dots):
    x_list = []
    y_list = []
    for x,y in dots:
        x_list.append(x)
        y_list.append(y)
        
        width = max(x_list) - min(x_list)
        height = max(y_list) - min(y_list)
    return width * height