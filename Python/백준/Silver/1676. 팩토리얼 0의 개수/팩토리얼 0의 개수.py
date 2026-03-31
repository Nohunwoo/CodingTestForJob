n = int(input())
fac = 1
for i in range(1,n+1):
    fac *= i

fac_list = list(str(fac))
count = 0
for i in range(len(fac_list),0,-1):
    if fac_list[i-1] != '0':
        break
    count +=1

print(count)