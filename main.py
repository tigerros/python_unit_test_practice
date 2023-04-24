import unittest
from sample_math import *
from math import *


class Vector2DTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_vector1 = Vector2D(7.84, -30)
        self.sample_vector2 = Vector2D(-81.7, -390.1)
        self.sample_vector3 = Vector2D(1, 2)
        self.sample_vector4 = Vector2D(0, 0)
        self.vectors = [self.sample_vector1, self.sample_vector2, self.sample_vector3, self.sample_vector4]
        self.lerp_alphas = [-8, 0, 0.00005, 0.12223, 0.44444, 0.5, 0.50009, 0.7, 0.899, 0.9, 1, 999]

    def test_magnitude(self):
        for vector in self.vectors:
            self.assertAlmostEqual(vector.magnitude(), sqrt(vector.x ** 2 + vector.y ** 2))

    def test_dot(self):
        for vi in range(len(self.vectors) - 1):
            current = self.vectors[vi]
            next_v = self.vectors[vi + 1]

            self.assertAlmostEqual(current.dot(next_v), (current.x * next_v.x) + (current.y * next_v.y))

    def test_lerp(self):
        for vi in range(len(self.vectors) - 1):
            current = self.vectors[vi]
            next_v = self.vectors[vi + 1]

            for lerp_alpha in self.lerp_alphas:
                lerped = current.lerp(next_v, lerp_alpha)
                lerped_correct = Vector2D(((1 - lerp_alpha) * current.x) + (lerp_alpha * next_v.x),
                                          ((1 - lerp_alpha) * current.y) + (lerp_alpha * next_v.y))
                self.assertAlmostEqual(lerped.x, lerped_correct.x)
                self.assertAlmostEqual(lerped.y, lerped_correct.y)


if __name__ == "__main__":
    unittest.main()
