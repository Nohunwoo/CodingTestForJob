a, b= map(int,input().split())
a = list(str(a))
b = list(str(b))

imsi = []
imsi = a[0]
a[0] = a[2]
a[2] = imsi

imsi = b[0]
b[0] = b[2]
b[2] = imsi

a= ''.join(a)
b= ''.join(b)

print (max(a,b))