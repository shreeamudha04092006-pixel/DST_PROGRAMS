class Transaction:
    def __init__(self, txn_id, customer, price, qty, discount):
        self.txn_id = txn_id
        self.customer = customer
        self.price = price
        self.qty = qty
        self.discount = discount

        self.__net_total = (price * qty) * (1 - discount)

    def get_net_total(self):
        return self.__net_total

    def to_dict(self):
        return {
            "txn_id": self.txn_id,
            "customer": self.customer,
            "net_total": self.__net_total
        }


txn = Transaction("TXN_501", "Asha", 500.0, 2, 0.10)

print(txn.get_net_total())
print(txn.to_dict())