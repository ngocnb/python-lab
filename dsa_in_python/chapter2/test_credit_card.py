import pytest
from credit_card import CreditCard


class TestCreditCardCharge:
    @pytest.fixture
    def card(self):
        """Fixture providing a card with a 1000 limit and 0 balance."""
        # Assuming your constructor looks like: CreditCard(customer, bank, acnt, limit)
        return CreditCard("John Doe", "Bank of Python", "1234 5678 9012 3456", 1000)

    def test_charge_success(self, card):
        """Standard valid charge within limit."""
        assert card.charge(100) is True
        assert card.get_balance() == 100

    def test_charge_denied_over_limit(self, card):
        """Charge that exceeds the credit limit."""
        assert card.charge(1100) is False
        assert card.get_balance() == 0

    @pytest.mark.parametrize("invalid_input", ["100", None, [100], True])
    def test_charge_invalid_types(self, card, invalid_input):
        """Ensure non-numeric types return False."""
        assert card.charge(invalid_input) is False

    def test_charge_float_value(self, card):
        """Verify float values are processed correctly."""
        assert card.charge(50.5) is True
        assert card.get_balance() == 50.5


class TestCreditCardPayment:
    @pytest.fixture
    def card(self):
        """Fixture providing a card with a 1000 limit and 0 balance."""
        return CreditCard("Jane Doe", "Bank of Python", "9876 5432 1098 7654", 1000)

    def test_make_payment_reduces_balance(self, card):
        """Verify that making a payment reduces the balance."""
        card.charge(500)
        card.make_payment(200)
        assert card.get_balance() == 300

    @pytest.mark.parametrize("invalid_payment", ["100", None, [100], True, -50])
    def test_make_payment_invalid_types(self, card, invalid_payment):
        """Ensure non-numeric or negative payments raise ValueError."""
        with pytest.raises(ValueError):
            card.make_payment(invalid_payment)

    def test_make_payment_float_value(self, card):
        """Verify float payment values are processed correctly."""
        card.charge(300.75)
        card.make_payment(100.25)
        assert card.get_balance() == 200.5

class TestCreditCardBalanceInitialization:
    def test_initial_balance_zero(self):
        """Verify that a new card has an initial balance of zero."""
        card = CreditCard("Alice Smith", "Bank of Python", "5555 6666 7777 8888", 1500)
        assert card.get_balance() == 0

    def test_initial_balance_custom(self):
        """Verify that a new card can be initialized with a custom balance."""
        card = CreditCard("Bob Smith", "Bank of Python", "9999 0000 1111 2222", 1500, balance=200)
        assert card.get_balance() == 200
    
    @pytest.mark.parametrize("invalid_balance", ["100", None, [100], True])
    def test_initial_balance_invalid_types(self, invalid_balance):
        """Ensure non-numeric initial balances raise ValueError."""
        with pytest.raises(ValueError):
            CreditCard("Charlie Brown", "Bank of Python", "3333 4444 5555 6666", 1500, balance=invalid_balance)