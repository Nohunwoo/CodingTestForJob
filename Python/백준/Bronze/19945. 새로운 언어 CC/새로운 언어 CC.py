ezin = int(input())
if ezin < 0:
    print(32)
elif ezin == 0:
    print(1)
else:
    tenzin = ''
    while (ezin // 2) > 0:
        tenzin += str(ezin % 2)
        ezin = ezin // 2
        
    tenzin = tenzin + "1"
    print(len(tenzin))