digit_sum = int(input().strip())
answer = 0
for i in range(digit_sum):
    mini_ds = sum(map(int, str(i)))
    if i + mini_ds == digit_sum:
        answer += i
        break
        
print(answer)