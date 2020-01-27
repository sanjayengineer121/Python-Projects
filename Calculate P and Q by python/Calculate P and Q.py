p=int(input("Value Of P\t\t\t\t"))
for m in range(2,p):
    if (p%m)==0:
        print("not Valid value of P")
        break
else:
    print("valid Value of P")
q=int(input("Value of Q \t\t\t\t"))

for k in range(2,q):
    if(q%k)==0:
        print("Not Valid Value of Q")
        break
else:
    print("valid value of Q")
n=p*q
n1=(p-1)*(q-1)

print("value of all possible e")

for e in range(1,n1+1):
    if e>1:
        for j in range(2,e):
            if(e%j)==0:
                break
        else:
            for k in range(1,100):
                for e in range(2,n1+1):
                    if(1+k*n1)%e==0:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                        print("value of e",e)
                        print("value of k",k)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("====================================================================\n")

ss="Written By Sanjay.11602079@lpu.in"
print(ss.center(40),"#")