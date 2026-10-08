amount = 3870

if amount % 10 != 0:
    print("Transaction rejected")
    
elif amount > 20000:
    print("Transaction rejected")
    
else:
    remaining = amount

    note500 = remaining // 500
    remaining = remaining % 500

    note200 = remaining // 200
    remaining = remaining % 200

    note100 = remaining // 100
    remaining = remaining % 100

    note50 = remaining // 50
    remaining = remaining % 50

    note10 = remaining // 10
    remaining = remaining % 10

    total_notes = note500 + note200 + note100 + note50 + note10

    print("₹500 notes :", note500)
    print("₹200 notes :", note200)
    print("₹100 notes :", note100)
    print("₹50 notes  :", note50)
    print("₹10 notes  :", note10)
    print("Total Notes:", total_notes)
    print("Amount     :", amount)