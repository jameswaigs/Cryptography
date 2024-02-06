letters = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                ciphertext += letters[new_index]
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                plaintext += letters[new_index]
    return plaintext


print("SIMPLE CAESAR CIPHER PROGRAM")
print("Do you want to encrypt or decrypt?")

user_input = input(str("e/d:  "))

if user_input == "e":
    print("ENCRYPTION MODE SELECTED")
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f"CIPHERTEXT: {ciphertext}")

elif user_input == "d":
    print("DECRYPTION MODE SELECTED")
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text, key)
    print(f"PLAINTEXT: {plaintext}")
