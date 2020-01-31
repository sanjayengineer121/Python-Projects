def rotate(input1,sl):
    Lfirst = input1[0 : sl]
    LSecond = input1[sl :]
    Rfir = input1[0 : len(input1)-sl]
    Rsecond = input1[len(input1)-sl : ]
    print("====================================================")
    print("Left Rotate :",LSecond+Lfirst)
    print("====================================================")
    print("Right Rotate :",Rsecond+Rfir)
    
if __name__ == "__main__":
    print("====================================================")
    input1=input("Inter String---------->")
    print("====================================================")
    for sl in range(1,len(input1)):
                    rotate(input1,sl)
