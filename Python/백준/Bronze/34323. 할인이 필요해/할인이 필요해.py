discount, things, price = map(int, input().split())

M_1 = things * price
N_discount = (price * (things+1))*(100-discount)//100

print(min(M_1, N_discount))