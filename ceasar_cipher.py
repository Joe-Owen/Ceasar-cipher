key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!"£$%^&*()-=_+[]{};@#:~`¬,./<>?\|'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext:
        try:
            i = (key.index(l) + n) % 96
            result += key[i]
        except ValueError:
            result += l

    return result


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 96
            result += key[i]
        except ValueError:
            result += l

    return result

def program():    
    code = input("Enter sentence to be ciphered or unciphered: ")
    print('\n'*99999)
    print("enter cipher level")
    level = 0
    x = 0
    while x == 0:
        try:
            level = int(input())
            
            if level >= 0:
                x = 1
        except: ValueError
        if x == 0:
            print("Invalid input\nnumber must be a whole positive number ")
    encryption = encrypt(level, code)
    decryption = decrypt(level, code)

    yn = input("do you want the code to be ciphered or unciphered c/u").lower()
    while yn not in ["c", "u"]:
        print("invalid")
        yn = input("do you want the code to be ciphered or unciphered y/n").lower()
    if yn == "c":
        print(encryption)
   
    if yn == "u":
        print(decryption)
    program()

program()
    


