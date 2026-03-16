n, zinbub = map(str, input().split())
n_list = list(n)
# ord('A') = 65 ord('Z') = 90
# 여기서 A는 10에 Z는 35
ten_zinbub = 0
for i in range(len(n_list)):
    if n_list[i].isalpha():
        n_list[i] = ord(n_list[i]) - 55
        ten_zinbub += int(n_list[i])*(int(zinbub)**(len(n_list)-i-1))
    else :
        ten_zinbub += int(n_list[i])*(int(zinbub)**(len(n_list)-i-1))
        
print(ten_zinbub)