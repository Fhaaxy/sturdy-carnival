import codecs
import base64
import morse_talk
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



#Morse Code
def morse_encrypt(text):
    return morse_talk.encode(text)

def morse_decrypt(text):
    return morse_talk.decode(text)



#Atbash
def atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97
            result += chr(base + (25 - (ord(char) - base)))
        else:
            result += char
    return result



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
        print("1) Ceasar Cipher")
        print("2) ROT13")
        print("3) Base64")
        print("4) Morse Code")
        print("5) Atbash")
        print("0) Back")

        decryption = input().upper()

        while True:
            if decryption == "1":
                print("Ceasar Cipher:")
                text = input("Insert Text: ")
                shift = int(input("Select Shift: "))
                print(ceasar_decrypt(text, shift))
                break

            elif decryption == "2":
                print("ROT13")
                text = input("Insert Text: ")
                print(rot13_decrypt(text))
                break

            elif decryption == "3":
                print("Base64")
                text = input("Insert Text: ")
                print(base64_decrypt(text))
                break

            elif decryption == "4":
                print("Morse Code")
                text = input("Insert Text: ")
                print(morse_decrypt(text))
                break

            elif decryption == "5":
                print("Atbash")
                text = input("Insert Text: ")
                print(atbash(text))
                break

            elif decryption == "0":
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice1 == "E":
        print("Which type of Cryptography do you choose? ")
        print("1) Ceasar Cipher")
        print("2) ROT13")
        print("3) Base64")
        print("4) Morse Code")
        print("5) Atbash")
        print("6) Hash_Sha256")
        print("0) Back")

        encryption = input().upper()

        while True:
            if encryption == "1":
                print("Ceasar Cipher")
                text = input("Insert Text: ")
                shift = int(input("Select Shift: "))
                print(caesar_encrypt(text, shift))
                break

            elif encryption == "2":
                print("ROT13")
                text = input("Insert Text: ")
                print(rot13_encrypt(text))
                break

            elif encryption == "3":
                print("Base64")
                text = input("Insert Text: ")
                print(base64_encrypt(text))
                break

            elif encryption == "4":
                print("Morse Code")
                text = input("Insert Text: ")
                print(morse_encrypt(text))
                break

            elif encryption == "5":
                print("Atbash")
                text = input("Insert Text: ")
                print(atbash(text))
                break

            elif encryption == "6":
                print("Hash_Sha256")
                text = input("Insert Text: ")
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