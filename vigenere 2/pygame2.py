import string

def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph


def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


def decrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += alph[new.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += alph[new.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


print("===============================================================================\n")
text1 = input("Enter Message for Encode ...\t\t\t\t")
print("===============================================================================\n")
key = input("Enter the key.......\t\t\t\t\t\t")

if len(key) <= len(text1):
    big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
    text_encrypt = encrypt(text1, big_key)

    print("===============================================================================\n")
    print('#======Vigenere Cipher(STEP 1) ======#')
    print('|----------------------------|')
    print('#========Start Encrypt=======#')
    print('|Your text: "' + str(text1) + '"')
    print('|Your key : "' + str(key) + '"')
    print('|Res      : ' + str(text_encrypt))
    print('|----------------------------|')
    print('#----------------------------#\n')
else:
    print('Error: len(key)>len(text) ')
    print("===============================================================================\n")

def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph


def encrypt1(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1:
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res


print("===============================================================================\n")
text2 = text_encrypt
print("===============================================================================\n")
key =  text1[::-1]

if len(key) <= len(text2):
    big_key = key * (len(text2) // len(key)) + key[:len(text2) % len(key)]
    text_encrypt = encrypt(text2, big_key)

    print("===============================================================================\n")
    print('#======Vigenere2 Cipher (STEP 2) ======#')
    print('|----------------------------|')
    print('#========Start Encrypt=======#')
    print('|Your text: "' + text2 + '"')
    print('|Your key : "' + key + '"')
    print('|Res      : ' + text_encrypt)
    print('|----------------------------|')
    print("===============================================================================\n")
