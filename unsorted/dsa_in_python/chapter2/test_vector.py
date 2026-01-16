import pytest
from vector import Vector

class TestVector:
    @pytest.fixture
    def vector_3d(self):
        """Fixture to provide a standard 3-dimensional vector for testing."""
        return Vector(3)

    # --- Constructor Tests ---

    def test_constructor_initialization(self, vector_3d):
        """Verify that the constructor initializes a vector of zeros."""
        assert len(vector_3d) == 3
        assert all(coord == 0 for coord in vector_3d._coords)

    # --- Get Item Tests ---

    def test_get_item(self, vector_3d):
        """Verify that __getitem__ retrieves the correct coordinate."""
        vector_3d._coords = [1, 2, 3]
        assert vector_3d[0] == 1
        assert vector_3d[1] == 2
        assert vector_3d[2] == 3

    # --- Set Item Tests ---

    def test_set_item(self, vector_3d):
        """Verify that __setitem__ updates the correct coordinate."""
        vector_3d[0] = 5
        vector_3d[1] = 10
        vector_3d[2] = 15
        assert vector_3d._coords == [5, 10, 15]

    # --- Addition Tests ---

    def test_addition_valid(self, vector_3d):
        """Verify that adding two vectors of the same dimension works correctly."""
        vec_a = Vector(3)
        vec_b = Vector(3)
        vec_a._coords = [1, 2, 3]
        vec_b._coords = [4, 5, 6]
        result = vec_a + vec_b
        assert result._coords == [5, 7, 9]

    def test_addition_invalid_dimension(self, vector_3d):
        """Verify that adding vectors of different dimensions raises ValueError."""
        vec_a = Vector(3)
        vec_b = Vector(4)
        with pytest.raises(ValueError):
            _ = vec_a + vec_b

    # --- Equality Tests ---
    def test_equality_true(self, vector_3d):
        """Verify that two identical vectors are considered equal."""
        vec_a = Vector(3)
        vec_b = Vector(3)
        vec_a._coords = [1, 2, 3]
        vec_b._coords = [1, 2, 3]
        assert vec_a == vec_b

    def test_equality_false(self, vector_3d):
        """Verify that two different vectors are not considered equal."""
        vec_a = Vector(3)
        vec_b = Vector(3)
        vec_a._coords = [1, 2, 3]
        vec_b._coords = [4, 5, 6]
        assert vec_a != vec_b

    # --- String Representation Tests ---
    def test_string_representation(self, vector_3d):
        """Verify that the string representation of the vector is correct."""
        vector_3d._coords = [1, 2, 3]
        assert str(vector_3d) == "<1,2,3>"