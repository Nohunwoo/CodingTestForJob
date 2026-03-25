n,k,p = map(int, input().split())
bbang = list(map(int, input().split()))

can_sell = 0
for i in range(n): 
    test_bbang = bbang[0+k*i:k+k*i] 
    no_cream = 0
    for i in test_bbang:
        if i == 0:
            no_cream +=1
    if no_cream < p :
        can_sell +=1

print(can_sell)