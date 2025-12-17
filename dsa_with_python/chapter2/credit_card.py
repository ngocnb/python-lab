class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman )
        bank
        the name of the bank (e.g., California Savings )
        acnt
        the acount identiﬁer (e.g., 5391 0375 9387 5309 )
        limit
        credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming suﬃcient credit limit.
        Return True if charge was processed; False if charge was denied.
        """

        # Booleans are numbers, but they aren't valid prices.
        # So we need to rule them out separately.
        # Also rule out negative prices.
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price < 0:
            return False

        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""

        # Ensure the payment amount is a positive number and not a boolean.
        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
            or amount < 0
        ):
            raise ValueError("Payment amount must be a positive number.")

        self._balance -= amount
