from sympy import primerange
import random

def randomChoice():
    if random.randint(0, 1) == 1:
        return True
    else:
        return False

# Clase para crear Incógnitas
class XVar:

    def __init__(self, parent, multiplier: int, power: int):
        self.parent = parent
        self.power = power
        self.multiplier = multiplier
        self.grade = power

    def __str__(self):
        return f"{abs(self.multiplier) if abs(self.multiplier) != 1 else None}x^{self.grade if self.grade != 0 else None}"

    def __neg__(self):
        self.multiplier = -self.multiplier
        return self

    def __mul__(self, other):
        if type(self) == type(other):
            self.multiplier *= other.multiplier
            self.power += other.power
            return self
        else:
            return self.multiplier * other if isinstance(other, int) or isinstance(other, float) else other * self

    def __truediv__(self, other):
        self.multiplier = Fraction(self.parent, [self.multiplier], other)
        return self

    def __int__(self):
        return self.multiplier

    def __lt__(self, other):
        if other == 0:
            if self.multiplier < 0:
                return True
            else:
                return False


class Group:

    def __init__(self, parent, elements: list = [], multiplier: int = 1, power: int = 1, locked: bool = False):
        self.parent = parent
        self.multiplier = multiplier
        self.elements = elements
        self.power = power
        self.locked = locked

    def __mul__(self, other):
        if randomChoice():
            self.multiplier = other * self if isinstance(other, Fraction) else other * self.multiplier
        else:
            counter = 0
            for e in self.elements:
                self.elements[counter] = other * e
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

    def __str__(self):
        text = f"{abs(self.multiplier) if abs(self.multiplier) != 1 else None}("
        counter = 0
        for element in self.elements:
            if counter == 0:
                text += f"- {abs(element) if isinstance(element, int) else element}" if element < 0 else f"{element}"
            else:
                text += f" - {abs(element) if isinstance(element, int) else element}" if element < 0 else f" + {element}"
            counter += 1
        return text + ")"

    def common_factor(self):
        pass


# Clase para crear Fracciones
class Fraction:

    def __init__(self, parent, numerator: list | Group, denominator: list | Group, multiplier: int = 1, power: int = 1):
        self.multiplier = multiplier
        self.power = power
        self.parent = parent
        self.numerator = Group(self.parent, numerator, 1, 1, True) if isinstance(numerator, list) else numerator
        self.denominator = Group(self.parent, denominator, 1, 1, True) if isinstance(denominator, list) else denominator

    def __mul__(self, other):
        if isinstance(other, Group):

        elif isinstance(other, Fraction):
            self.numerator = self.numerator * other.numerator
            self.denominator = self.denominator * other.denominator
        else:
            self.numerator = self.numerator * other
        return self

    def __truediv__(self, other: int):
        self.denominator = self.denominator * other
        return self

    def simplify(self):
        self.factor(True, True)

        numeratorList = []
        primeList = primerange(2, self.numerator.multiplier)
        for prime in primeList:
            while True:
                if self.numerator.multiplier % prime == 0:
                    numeratorList.append(prime)
                    self.numerator.multiplier /= prime
                else:
                    break

        denominatorList = []
        primeList = primerange(2, self.denominator.multiplier)
        for prime in primeList:
            while True:
                if self.denominator.multiplier % prime == 0:
                    denominatorList.append(prime)
                    self.denominator.multiplier /= prime
                else:
                    break

        for prime in numeratorList:
            if prime in denominatorList:
                numeratorList.remove(prime)
                denominatorList.remove(prime)

        for num in numeratorList:
            self.numerator.multiplier *= num

        for den in denominatorList:
            self.denominator.multiplier *= den


    def factor(self, bnumerator: bool, bdenominator: bool):
        if bnumerator:
            counter = 0
            for element in self.numerator.elements:
                elementList = []
                primeList = primerange(2, element)

                if element == 0 or element == 1:
                    elementList.append(element)

                else:
                    for prime in primeList:
                        while True:
                            if element % prime == 0:
                                elementList.append(prime)
                                element /= prime
                            else:
                                break

                if element == 1 or element == 0:
                    self.numerator.elements[counter] = elementList

                counter += 1

            for element in self.numerator.elements:
                for prime in element:
                    notFactorable = False
                    for element2 in self.numerator.elements:
                        if not prime in element2:
                            notFactorable = True

                    if not notFactorable:
                        self.numerator.multiplier *= prime
                        for everyList in self.numerator.elements:
                            everyList.remove(prime)

        if bdenominator:
            counter = 0
            for element in self.denominator.elements:
                elementList = []
                primeList = primerange(2, element)

                if element == 0 or element == 1:
                    elementList.append(element)

                else:
                    for prime in primeList:
                        while True:
                            if element % prime == 0:
                                elementList.append(prime)
                                element /= prime
                            else:
                                break

                if element == 1 or element == 0:
                    self.denominator.elements[counter] = elementList

                counter += 1

            for element in self.denominator.elements:
                for prime in element:
                    notFactorable = False
                    for element2 in self.denominator.elements:
                        if not prime in element2:
                            notFactorable = True

                    if not notFactorable:
                        self.numerator.multiplier *= prime
                        for everyList in self.denominator.elements:
                            everyList.remove(prime)

    def __str__(self):
        return f"{abs(self.multiplier) if abs(self.multiplier) != 1 else None}({self.numerator}/{self.denominator})"

    def __neg__(self):
        self.multiplier = -self.multiplier
        return self

    def __lt__(self, other):
        if other == 0:
            if self.multiplier < 0:
                return True
            else:
                return False