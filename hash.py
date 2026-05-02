import hashlib

print("Welcome to Hash MD5 :)")

try:
    text = str(input("Inform the text: "))
    before = text
    text_encrypted = hashlib.md5(text.encode())
    text_encrypted = text_encrypted.hexdigest()
    encry_list = text_encrypted

    while True:    
        try:
            
            if len(text) == 0:
                print("Empty Field")
                break

            option = int(input("\nOptions:\n1 - text encrypted\n2 - text decrypted\n3 - new text\n4 - exit\n"))
            if option == 1:
                print(f"--Text Encrypted--\nText : {encry_list}")

            elif option == 2:
                print(f"--Text Decrypted--\nText: {before}")
            
            elif option == 3:    
                text = str(input("Inform the text: "))
                before = text
                text_encrypted = hashlib.md5(text.encode())
                text_encrypted = text_encrypted.hexdigest()
                encry_list = text_encrypted
            
            elif option == 4:
                print("--Exit--\nGoodbye :)")
                break
            
            else:
                print("ERROR\nTry again")
        except ValueError:
            print("ERROR\nEnter a valid value")
            break

except ValueError :
    print("ERROR\nTry again")



    

