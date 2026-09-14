class Payment:
    """Parent class defining the payment-processing interface."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using a general payment method")


class CreditCardPayment(Payment):
    """Payment processed through a credit card."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Credit Card")


class UPIPayment(Payment):
    """Payment processed through UPI."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using UPI")


class NetBankingPayment(Payment):
    """Payment processed through net banking."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Net Banking")


class WalletPayment(Payment):
    """Payment processed through a digital wallet."""

    def process_payment(self, amount):
        print(f"Processing ₹{amount} using Wallet")


def main():
    payments = [
        CreditCardPayment(),
        UPIPayment(),
        NetBankingPayment(),
        WalletPayment(),
    ]

    print("Payment processing demonstration:")
    for payment in payments:
        payment.process_payment(5000)


if __name__ == "__main__":
    main()
