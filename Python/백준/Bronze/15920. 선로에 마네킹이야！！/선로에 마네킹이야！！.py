n = int(input())
x = input()
status = 2
time = 0
for i in x :
    if i == "W":
        time +=1
        if time == 2:
            break
    if i == "P" and status == 1:
        status = 2
    elif i == "P" and status == 2:
        status = 1
    if i == "P" and time == 1:
        status = 3

if time < 2:
    print("0")
elif time == 2 and status == 1:
    print("1")
elif time == 2 and status == 2:
    print("5")
elif time == 2 and status == 3:
    print("6")