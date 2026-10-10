password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

length_ok = len(password) >= 8

if upper and lower and digit and special and length_ok:
    print("Valid password")
else:
    print("Invalid password")

print("Uppercase:", "Present" if upper else "Missing")
print("Lowercase:", "Present" if lower else "Missing")
print("Digit:", "Present" if digit else "Missing")
print("Special character:", "Present" if special else "Missing")
print("Minimum length:", "Satisfied" if length_ok else "Not satisfied")