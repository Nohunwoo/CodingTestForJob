numbers = input().split()
n = int(input()) 
numbers[1] = int(numbers[1])+ n
numbers[0] = int(numbers[0])+ int(numbers[1]) // 60

while numbers[1] >= 60 :
    numbers[1] = int(numbers[1]) % 60

if numbers[0] > 23:
    numbers[0] = numbers[0] - 24
print(*numbers)