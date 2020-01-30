def gcd(p,q):
    if(q==0):
        return p
    return gcd(q, p%q)

print("===============================================\n")
p=int(input("Input Intier Number 1 --->"))
print("===============================================\n")
q=int(input("Input Intier Number 2 --->"))
if (gcd(p,q)):
    
    print("===============================================\n")

    print("gcd of ",p, "and" , q, "is ---->",gcd(p,q))
else:
    print("GCD Not Found")
