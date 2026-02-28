up, down, height = map(int, input().split())
day = (height - down) // (up - down) 

if (height - down) % (up - down) != 0:
    day += 1

print(day)