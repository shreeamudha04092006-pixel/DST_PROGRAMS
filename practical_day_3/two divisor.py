n = int(input("N: "))

divisor1 = int(input("Divisor 1: "))
word1 = input("Word 1: ")

divisor2 = int(input("Divisor 2: "))
word2 = input("Word 2: ")

for i in range(1, n + 1):

    if i % divisor1 == 0 and i % divisor2 == 0:
        print(word1 + word2)

    elif i % divisor1 == 0:
        print(word1)

    elif i % divisor2 == 0:
        print(word2)

    else:
        print(i)