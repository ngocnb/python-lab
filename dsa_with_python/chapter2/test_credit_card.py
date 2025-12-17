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
