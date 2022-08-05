q = int(input("Enter a prime number q: "))
alpha = int(input("Enter primitive root of q: "))
xa = int(input("Enter private key A: "))
xb = int(input("Enter private key B: "))

ya = ((alpha ** xa) % q)
yb = ((alpha ** xb) % q)

key = ((ya ** xb) % q)

print(f"Public key A: {ya}")
print(f"Public Key B: {yb}")
print(f"Secret key K: {key}")
