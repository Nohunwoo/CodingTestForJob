def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isalpha():
            my_string = my_string.replace(char, ' ')
    num = my_string.split()
    answer = sum(int(n) for n in num)
    return answer