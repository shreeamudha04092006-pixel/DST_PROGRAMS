def calculate_bill(prices, tax_rate=0.10, discount=0.20):

    subtotal = sum(prices)

    discount_amount = subtotal * discount

    after_discount = subtotal - discount_amount

    tax = after_discount * tax_rate

    final_total = after_discount + tax

    print("Subtotal:", subtotal)
    print("Discount:", discount_amount)
    print("Tax:", tax)
    print("Final total:", final_total)


prices = [100, 50]

calculate_bill(prices, tax_rate=0.10, discount=0.20)