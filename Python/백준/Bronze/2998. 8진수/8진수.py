# Bronze 2

binary = input()

if len((binary)) % 3 != 0:
    need_zero = 3 - len((binary)) % 3
    binary = binary.zfill(len(binary)+need_zero)

octal_dic = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
answer = ""

for i in range(0, len(binary), 3):
    chunk = binary[i : i+3]  
    
    answer += octal_dic[chunk]

print(answer)
