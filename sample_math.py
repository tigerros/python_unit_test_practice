import math


class Vector2D:
    """A vector representation in 2D space, with the origin being (0,0)."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def magnitude(self) -> float:
        """Returns the magnitude (length) of the vector."""
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def dot(self, other: 'Vector2D') -> float:
        """Returns the dot product of the two vectors. In other words, ``(ax * bx) + (ay * by)``."""
        return (self.x * other.x) + (self.y * other.y)

    def lerp(self, other: 'Vector2D', alpha: float) -> 'Vector2D':
        """Returns a vector linearly interpolated vector between this vector and the given vector by the given alpha."""
        return Vector2D(((1 - alpha) * self.x) + (alpha * other.x), ((1 - alpha) * self.y) + (alpha * other.y))