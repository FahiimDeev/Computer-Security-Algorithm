letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    cipherText = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            new_index = (index + key) % num_letters
            cipherText += letters[new_index]
        else:
            cipherText += ' '
    return cipherText

def decrypt(cipherText, key):
    plaintext = ''
    for letter in cipherText:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            new_index = (index - key) % num_letters
            plaintext += letters[new_index]
        else:
            plaintext += ' '
    return plaintext



print("do you wanna encrypt or decrupt? ")
user_input = input('e/d: ').lower()
print()

if (user_input == 'e'):
    print("Encryption Mood")
    print()
    key = int(input("key for encryption from 1 to 26: "))
    text = input("enter the text to encrypt: ")
    ciphertext = encrypt(text,key)
    print(f'Ciphertext: {ciphertext}')
    
elif (user_input=='d'):
    print("Decryption Mood")
    print()
    key = int(input("key for decryption from 1 to 26: "))
    text = input("enter a text for decryption: ")
    plaintext = decrypt(text,key)
    print(f'Plaintext: {plaintext}')
    