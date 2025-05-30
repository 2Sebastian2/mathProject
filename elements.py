from main import Equation
import random

def randomChoice():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False

# Clase para crear Incógnitas
class XVar:

    def __init__(self, parent: Equation, multiplier: int, power: int):
        self.parent = parent
        self.multiplier = multiplier
        self.grade = power

    def __str__(self, init: bool = False):
        if init:
            return (f"{abs(self.multiplier)}x^{self.grade}" if self.grade != 1 else f"{abs(self.multiplier)}x") if self.multiplier != 1 else (f"x^{self.grade}" if self.grade != 1 else f"x")
        else:
            return (
                f" {abs(self.multiplier)}x^{self.grade}" if self.grade != 1 else f" {abs(self.multiplier)}x") if self.multiplier != 1 else (f" x^{self.grade}" if self.grade != 1 else f" x")

    def __neg__(self):
        self.multiplier = -self.multiplier
        return self

    def __mul__(self, other):
        return other * self.multiplier

    def __truediv__(self, other):
        self.multiplier = Fraction(self.parent, [self.multiplier], other)
        return self


class Group:

    def __init__(self, parent: Equation, elements: list = [], multiplier: int = 1, power: int = 1, locked: bool = False):
        self.parent = parent
        self.multiplier = multiplier
        self.elements = elements
        self.power = power
        self.locked = locked

    def __mul__(self, other):
        if randomChoice():
            self.multiplier *= other
        else:
            counter = 0
            for e in self.elements:
                self.elements[counter] = e * other
                counter += 1
            if self.locked:
                pass
            elif randomChoice():
                pass
            else:
                for e in self.elements:
                    self.getLocation().insert(self.getLocation().index(self), e)
                self.getLocation().remove(self)
        return self

    def __neg__(self):
        if randomChoice():
            self.multiplier = -self.multiplier
        else:
            counter = 0
            for e in self.elements:
                self.elements[counter] = -e
                counter += 1
        return self

    def __truediv__(self, other):
        return Fraction(self.parent, self, [other] if not isinstance(other, Group) else other)

    def getLocation(self):
        if self in self.parent.left:
            return self.parent.left
        elif self in self.parent.right:
            return self.parent.right
        else:
            raise Exception("Object was not found in parent group.")

    def common_factor(self):
        pass


# Clase para crear Fracciones
class Fraction:

    def __init__(self, parent: Equation, numerator: list | Group, denominator: list | Group, multiplier: int = 1, power: int = 1):
        self.multiplier = multiplier
        self.power = power
        self.parent = parent
        self.numerator = Group(self.parent, numerator, 1, 1, True) if isinstance(numerator, list) else numerator
        self.denominator = Group(self.parent, denominator, 1, 1, True) if isinstance(denominator, list) else denominator

    def __mul__(self, other):
        if randomChoice():
            self.multiplier *= other
        elif isinstance(other, Fraction):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
        else:
            self.numerator += other
        return self

    def divide(self):
        return