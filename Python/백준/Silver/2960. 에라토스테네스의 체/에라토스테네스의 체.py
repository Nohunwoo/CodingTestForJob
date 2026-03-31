n, erase = map(int, input().split())

is_active = [True] * (n + 1)
count = 0

for i in range(2, n + 1):
    if is_active[i]:
        for j in range(i, n + 1, i):
            if is_active[j]:
                is_active[j] = False 
                count += 1 

                if count == erase:
                    print(j)
                    exit()