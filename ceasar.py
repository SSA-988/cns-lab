key = int(input("Enter Key: "))
plain = input("Enter Text: ").upper()
cipher = ""

for i in plain:
    cipher += chr(((ord(i) + key - 65) % 26) + 65)

print(f"Cipher Text: {cipher}")
