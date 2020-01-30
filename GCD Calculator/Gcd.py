def gcd(a,b):
    if (a==0):
        return b
    if (b==0):
        return a
    if (a==b):
        return a
    if (a>b):
        return gcd(a-b, b)
    return gcd(a, b-a)
print("===============================================\n")
a=int(input("Enter Number 1 --->"))

print("===============================================\n")
b=int(input("Enter Number 2 --->"))
if (gcd(a, b)):
    print("===============================================\n")
    print('GCD of',a, 'and' ,b, 'is <---->' ,gcd(a, b))
else:
    print("Not Found")
