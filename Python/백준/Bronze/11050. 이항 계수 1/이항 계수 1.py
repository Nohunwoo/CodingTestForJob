n, k = map(int, input().split())

n_fac = 1
k_fac = 1
nk_fac = 1

for i in range(1,n+1):
    n_fac *=i #120
    
for i in range(1,k+1):
    k_fac *= i #2
    
for i in range(1,n-k+1):
    nk_fac *= i #6
answer = 0 
answer = n_fac // (k_fac * nk_fac) #120/(2*6)

print(answer)