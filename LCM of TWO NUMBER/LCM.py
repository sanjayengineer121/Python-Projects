def gcd(p,q):
    if(p==0):
        return q
    return gcd(q % p, p)


def LcM(p,q):
    return (p*q)/gcd(p,q)

print("===============================================\n")
p=int(input("Input Intier Number 1 --->"))
print("===============================================\n")
q=int(input("Input Intier Number 2 --->"))    
print("===============================================\n")

print("LCM of ",p, "and" , q, "is ---->",LcM(p,q))
