star = int(input())
star_print =''
for i in range(star):
    star_print = " "*(star-i-1)+"*"*(2*i+1)
    if i < star-1:
        star_print = star_print[:star-i] + " "*(2*i-1) + star_print[star:star+1]
    print(star_print)