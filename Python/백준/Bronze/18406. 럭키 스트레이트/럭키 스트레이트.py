islucky = input()
first_half = 0
second_half = 0

for i in range(0,len(islucky)//2):
    first_half += int(islucky[i])

for i in range(len(islucky)//2, len(islucky)):
    second_half += int(islucky[i])

if first_half == second_half:
    print('LUCKY')
else :
    print('READY')