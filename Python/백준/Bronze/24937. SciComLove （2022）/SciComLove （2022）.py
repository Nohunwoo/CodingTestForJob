n= int(input())
sen = 'SciComLove'

if n > 10 :
    n = n%10
    print(sen[n:10] + sen[0:n])
else :
    print(sen[n:10] + sen[0:n])