import pytest

from flower import Flower


class TestFlower:
    @pytest.fixture
    def default_flower(self):
        """Fixture to provide a standard flower instance for testing."""
        return Flower("Rose", 32, 5.50)

    # --- Constructor Tests ---

    def test_constructor_initialization(self, default_flower):
        """Verify that the constructor sets initial values correctly."""
        assert default_flower.get_name() == "Rose"
        assert default_flower.get_petals() == 32
        assert default_flower.get_price() == 5.50

    # --- Name Method Tests ---

    def test_set_and_get_name(self, default_flower):
        """Verify name setter and getter."""
        default_flower.set_name("Lily")
        assert default_flower.get_name() == "Lily"

    # --- Petal Method Tests ---

    def test_set_and_get_petals(self, default_flower):
        """Verify petals setter and getter."""
        default_flower.set_petals(15)
        assert default_flower.get_petals() == 15

    # --- Price Method Tests ---

    def test_set_and_get_price(self, default_flower):
        """Verify price setter and getter."""
        default_flower.set_price(12.99)
        assert default_flower.get_price() == 12.99

    # --- Data Type Validation ---

    def test_variable_types(self, default_flower):
        """Verify that the instance variables return the expected types."""
        assert isinstance(default_flower.get_name(), str)
        assert isinstance(default_flower.get_petals(), int)
        assert isinstance(default_flower.get_price(), float)
