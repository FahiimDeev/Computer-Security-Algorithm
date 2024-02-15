import math

# Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# # Function to perform encryption
# def encrypt(message, e, n):
#     return (message ** e) % n

# # Function to perform decryption
# def decrypt(ciphertext, d, n):
#     return (ciphertext ** d) % n

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Taking input for p and q
p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q

theta_n = (p - 1) * (q - 1)

print("The value of n is ", n)

# GCD function
def gcd(e, theta_n):
    if theta_n == 0:
        return e
    else:
        return gcd(theta_n, e % theta_n)

# Finding the e
e = None
while True:
    user_input = input("Enter e: ")
    try:
        e_candidate = int(user_input)  
        gcd_result = gcd(e_candidate, theta_n)
        if 1 < e_candidate < theta_n and gcd_result == 1:
            e = e_candidate
            break
        else:
            print("Invalid e")
    except ValueError:
        print("Invalid e")

print("Final value of e:", e)

public_key = f"Public key is ({e}, {n})"
print(public_key)

# Finding the d value
k = 0
while True:
    d = (1 + (k * theta_n)) / e
    if d.is_integer():
        d = int(d) 
        break
    k += 1

print("Final value of d is: ", d)
private_key = f"Private key is ({d}, {n})"
print(private_key)

# Encryption here
message = int(input("Enter the message to encrypt: "))
ciphertext = encrypt(message, e, n)
print(f"Encrypted message is {ciphertext}")

# Decryption here
decrypted_message = decrypt(ciphertext, d, n)
print(f"Decrypted message is {decrypted_message}")
