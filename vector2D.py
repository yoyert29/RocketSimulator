from dataclasses import dataclass
import math

@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other):
        return Vector2D(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector2D(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, scalar):
        return Vector2D(
            self. x * scalar,
            self. y * scalar
        )

    def __rmul__(self, scalar):
        return (self.__mul__(scalar))

    def __truediv__(self, scalar):
        return Vector2D(
            self.x / scalar,
            self.y / scalar
        )

    def __neg__(self):
        return(
            -self.x,
            -self.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"

    def dot(self, other):
        return (self.x * other.x + self.y * other.y)

    def cross(self, other):
        return (self.x * other.y - self.y * other.x)

    def magnitude(self):
        return (math.hypot(self.x, self.y))

    def angle(self):
        return (math.atan2(self.y, self.x))

    def to_polar(self):
        return (self.magnitude(), self.angle())

    def normalize(self):
        m = self.magnitude()
        if m == 0:
            return Vector2D(0,0)
        
        return (self.__truediv__(m))

    def angle_between(self, other):
        denominator = self.magnitude() * other.magnitude()

        if denominator == 0:
            return 0

        value = self.dot(other) / denominator

        value = max(-1, min(1, value))

        return math.acos(value)

    def perpendicular(self):
        return Vector2D(
            self.x,
            -self.y
        )

    