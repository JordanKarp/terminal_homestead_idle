class Wallet:
    """
    Stores player currency. Supports deposit, spend, check balance, and affordability checks.
    """

    def __init__(self, starting_amount=0):
        self.balance = starting_amount
        self.transactions = []

    def deposit(self, amount: int, memo: str = "Unknown Deposit") -> None:
        if amount < 0:
            raise ValueError("Cannot deposit negative currency.")
        self.balance += amount
        self.transactions.append((memo, amount))

    def spend(self, amount: int, memo: str = "Unknown Transaction") -> bool:
        """Attempt to spend currency. Returns True if successful, False if insufficient funds."""
        if amount < 0:
            raise ValueError("Cannot spend negative currency.")
        if self.can_afford(amount):
            self.balance -= amount
            self.transactions.append((memo, amount * -1))
            return True
        return False

    def can_afford(self, amount: int) -> bool:
        return self.balance >= amount

    def display_transactions(self):
        transaction_log = "".join(
            f"{memo}: {amount}\n" for memo, amount in self.transactions
        )
        print(transaction_log)

    def __repr__(self):
        return f"Wallet            $ {self.balance}"
