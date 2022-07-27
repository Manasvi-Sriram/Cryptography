
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    message=input(" Enter your message: ")
    key = int(input(" Enter your key(1-94): "))
    encryptedText = ""
    for i in range(len(message)):
        temp = (ord(message[i])+key)
        if(temp>126):
            temp=temp-127+32
        encryptedText+=chr(temp) 
    print(" Encrypted : "+encryptedText)
    main()       



    


def decryption():
    print(" Decryption")
    print("Message can only be lower or uppercase alphabet")
    encryptedMessage=input(" Enter encrypted text")
    decryptKey = int(input(" Enter key(1-94)"))
    decryptText=""
    for i in range(len(encryptedMessage)):
        temp = (ord(encryptedMessage[i])-decryptKey)
        if(temp<32):
            temp=temp+127-32
        decryptText+=chr(temp)
    print("Decrypted text :"+decryptText) 
    main()   




    
    

        
if __name__ == "__main__":
    main()
