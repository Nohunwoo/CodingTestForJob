n= int(input())

for i in range(n):
    ps_list = list(input())
    new_list = []
    for i in range(len(ps_list)):
        if new_list == []:
            new_list.append(ps_list[i])
        elif (new_list[-1]=='(') and (ps_list[i] == ')'):
            new_list.remove(new_list[-1])
        else:
            new_list.append(ps_list[i])
    if new_list == []:
        print("YES")
    else:
        print("NO")