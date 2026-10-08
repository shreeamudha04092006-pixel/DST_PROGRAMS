message = input("Message: ")
shift = int(input("Shift: "))

encrypted = ""

for ch in message:
    if 'A' <= ch <= 'Z':
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

print("Encrypted:", encrypted)

decrypted = ""

for ch in encrypted:
    if 'A' <= ch <= 'Z':
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch

print("Decrypted:", decrypted)