#asking for the prime numbers from Alice and Bob
p = int(input("Prime1: "))
q = int(input("Prime2: "))

#private keys for Alice and Bob
alice_key = int(input("Alice Key: "))
bob_key = int(input("Bob key: "))

#calculation of public values
alice = p ** alice_key % q
bob = p ** bob_key % q

#exchanging the keys
final_alice = bob ** alice_key % q
final_bob = alice ** bob_key % q

print("Final key for Alice:", final_alice)
print("Final key for Bob:", final_bob)
