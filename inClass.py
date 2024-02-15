import random
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the modular multiplicative inverse of a number
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('The modular inverse does not exist')
    else:
        return x % m

# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# Generate large prime numbers p and q
def generate_large_primes(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:
            p += 1
        if is_prime(p):
            return p

# Key size in bits
key_size = 2048

# Generate large prime numbers p and q
p = generate_large_primes(key_size // 2)
q = generate_large_primes(key_size // 2)

n = p * q
phi_n = (p - 1) * (q - 1)

# Choose a public exponent e (typically a small prime)
e = 65537  # Common choice for e

# Calculate the modular multiplicative inverse of e modulo phi_n to find d
d = mod_inverse(e, phi_n)

print("Public Key (e, n):", e, n)
print("Private Key (d, n):", d, n)
