import numpy as np


def getMat(text, add = 1):
    matrix = [[[0] for _ in range(N)] for __ in range((len(text) // N) + add)]
    i, j = 0, 0
    for el in text:
        if j < N - 1:
            matrix[i][j] = [(ord(el) - 65) % 26]
            j += 1
        else:
            matrix[i][j] = [(ord(el) - 65) % 26]
            i += 1
            j = 0
    return matrix


# setup
# N = 3
# mat = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
N = int(input("Enter the dimensions of key matrix: "))
mat = []
for i in range(0, N):
    mat.append([])
    for j in range(0, N):
        ele = int(input(f"Enter element [{i}][{j}]: "))
        mat[i].append(ele)
print(mat)

# mod inverse
det = np.linalg.det(mat)
modInverse = 0
for i in range(-26, 26):
    if (det * i) % 26 == 1:
        modInverse = i
        break
modInverse %= 26
cofactor = np.linalg.inv(mat) * det
inv = cofactor * modInverse
inv %= 26

# encryption
plaintext = input("Enter text: ").upper()
plainMat = getMat(plaintext)
encryptedText = ""
ans = [np.dot(np.array(mat) % 26, np.array(i) % 26) for i in plainMat]
for i in ans:
    for j in i:
        encryptedText += chr(int(round(j[0]) % 26) + 65)
print("Encrypted text:", encryptedText[0: len(plaintext)])

# decryption
encryptMat = getMat(encryptedText, 0)
decAns = [np.dot(np.array(inv) % 26, np.array(i) % 26) for i in encryptMat]

decrypted = ""
for i in decAns:
    for j in i:
        decrypted += chr(int(round(j[0]) % 26) + 65)

print("Decrypted Text:", decrypted[0: len(plaintext)])
