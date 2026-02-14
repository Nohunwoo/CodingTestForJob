n = int(input())

for _ in range(n):
    quart, dime, nick, penny = 0,0,0,0
    x = int(input())
    
    quart += x//25
    x = x % 25

    dime += x//10
    x = x % 10
    
    nick += x//5
    x = x % 5
    
    penny += x//1
        
    print(f'{quart} {dime} {nick} {penny}')