test_case = int(input())

for i in range(test_case):
    stage = int(input())
    room = int(input())
    apt = [x for x in range(1, room + 1)]
    for i in range(stage):
        for j in range(1,room):
            apt[j] = apt[j-1] + apt[j]
    print(apt[-1])