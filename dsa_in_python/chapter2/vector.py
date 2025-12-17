class Vector:
    """Represent a vector in multi-dimensional space"""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        result = self
        for j in range(len(self)):
            result[j] += other[j]

        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other  # delegate to __eq__

    def __str__(self):
        """Produce string representation of vector"""
        return "<" + ",".join(str(x) for x in self._coords) + ">"
