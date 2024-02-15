import math

#taking input for p and q
p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q

theta_n = (p - 1) * (q - 1)

print("The value of n is ", n)

#gcd function
def gcd(e, theta_n):
    if theta_n == 0:
        return e
    else:
        return gcd(theta_n, e % theta_n)

#finding the e
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
            print("Invalid value for e")
    except ValueError:
        print("Invalid input, enter a valid integer for e.")

print("Final value of e:", e)

public_key = f"Public key is ({e}, {n})"
print(public_key)

#finding the d
k=0
while True:
    d = (1 + (k * theta_n)) / e
    if d.is_integer():
        break
    k += 1
print("Final value of d is: ",d)
private_key = f"Private key is ({d}, {n})"
print(private_key)


