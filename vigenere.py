key = input("Enter the key: ").upper()
plain = input("Enter the message: ").upper()
cipher = ""

i = j = 0
while i < len(plain):
    while j < len(key) and i < len(plain):
        cipher += chr((ord(plain[i]) + ord(key[j])) % 26 + 65)
        i += 1
        j += 1
    j = 0

print(f"Cipher Text: {cipher}")
