import codecs
import base64
import hashlib


#Ceasar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97
            result += chr((ord(char) - base + shift) %26 + base)
        else:
            result += char
    return result

def ceasar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97
            result += chr((ord(char) - base - shift) %26 + base)
        else:
            result += char
    return result



#ROT13
def rot13_encrypt(text):
    return codecs.encode(text, "rot_13")

def rot13_decrypt(text):
    return codecs.decode(text, "rot_13")



#Base64
def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    return base64.b64decode(text.encode()).decode()



#Hashing (SHA256)
def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


#Start
print("Welcome to the Cryptography Program")

while True:
    print("Do you want Decrypt or Encrypt? D/E: ")
    print("0 to exit")
    choice1 = input().upper()

    if choice1 == "D":
        print("What is the method of encryption? ")
        print("A) Ceasar Cipher")
        print("B) ROT13")
        print("C) Base64")
        print("0) Back")

        decryption = input().upper()

        while True:
            if decryption == "A":
                print("Ceasar Cipher:")
                text = input("Insert Text:")
                shift = int(input("Select Shift: "))
                print(ceasar_decrypt(text, shift))
                break

            elif decryption == "B":
                print("ROT13")
                text = input("Insert Text:")
                print(rot13_decrypt(text))
                break

            elif decryption == "C":
                print("Base64")
                text = input("Insert Text:")
                print(base64_decrypt(text))
                break

            elif decryption == "0":
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice1 == "E":
        print("Which type of Cryptography do you choose? ")
        print("A) Ceasar Cipher")
        print("B) ROT13")
        print("C) Base64")
        print("D) Hash_Sha256")
        print("0) Back")

        encryption = input().upper()

        while True:
            if encryption == "A":
                print("Ceasar Cipher")
                text = input("Insert Text:")
                shift = int(input("Select Shift: "))
                print(caesar_encrypt(text, shift))
                break

            elif encryption == "B":
                print("ROT13")
                text = input("Insert Text:")
                print(rot13_encrypt(text))
                break

            elif encryption == "C":
                print("Base64")
                text = input("Insert Text:")
                print(base64_encrypt(text))
                break

            elif encryption == "D":
                print("Hash_Sha256")
                text = input("Insert Text:")
                print(hash_sha256(text))
                break

            elif encryption == "0":
                break

            else:
                print("Invalid choice. Please try again.")


    elif choice1 == "0":
        break

    else:
        print("Invalid choice. Please press D to decrypt or E to encrypt")
        print("0 to exit")