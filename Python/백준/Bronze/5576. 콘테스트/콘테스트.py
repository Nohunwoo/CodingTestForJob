a_list = []
b_list = []
for i in range(10):
    a_list.append(int(input()))
for i in range(10):
    b_list.append(int(input()))

a_list.sort(reverse = True)
b_list.sort(reverse = True)
a_answer = a_list[0] + a_list[1] + a_list[2]
b_answer = b_list[0] + b_list[1] + b_list[2]
print(f'{a_answer} {b_answer}')