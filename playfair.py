key = input("Enter the Keyword: ").upper().replace("J", "I")
plain = input("Enter the Plain Text: ").upper().replace("J", "I")
cipher = ""


def find(ch):
    res = []
    for a in range(0, 5):
        if ch in key_matrix[a]:
            res.append(a)
            res.append(key_matrix[a].index(ch))
    return res


key_list = []
for letter in key:
    if letter not in key_list:
        key_list.append(letter)

for letter in range(65, 91):
    if chr(letter) not in key_list:
        key_list.append(chr(letter))

key_list.remove('J')
key_matrix = []
k = 0
print("Key Matrix:")
for i in range(0, 5):
    temp = []
    for j in range(0, 5):
        temp.append(key_list[k])
        print(key_list[k], end = "  ")
        k += 1
    key_matrix.append(temp)
    print()

i = 0
while i < len(plain):
    if i == len(plain) - 1:
        plain = plain + 'X'
    if plain[i] == plain[i + 1]:
        plain = plain[:i + 1] + 'X' + plain[i + 1:]
    i += 2

for i in range(0, len(plain), 2):
    l1 = find(plain[i])
    l2 = find(plain[i + 1])
    if l1[0] == l2[0]:
        cipher += (key_matrix[l1[0]][(l1[1] + 1) % 5]) + (key_matrix[l2[0]][(l2[1] + 1) % 5])
    elif l1[1] == l2[1]:
        cipher += (key_matrix[(l1[0] + 1) % 5][l1[1]]) + (key_matrix[(l2[0] + 1) % 5][l2[1]])
    else:
        cipher += (key_matrix[l1[0]][l2[1]]) + (key_matrix[l2[0]][l1[1]])

print(f"\nCipher Text: {cipher}")
