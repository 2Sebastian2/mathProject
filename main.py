import random
from typing import Self


# Clase para crear Incógnitas
class XVar:

    def __init__(self, multiplier: int, grade: int):
        self.multiplier = multiplier
        self.grade = grade

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

    def __divmod__(self, other):
        self.multiplier = Fraction(self.multiplier, other, 1)
        return self

    def frac(self, denominator: int):
        self.multiplier = Fraction(self.multiplier, denominator, 1)


# Clase para crear Fracciones
class Fraction:

    def __init__(self, numerator: int | XVar, denominator: int | XVar, grade: int):
        self.numerator = numerator
        self.denominator = denominator
        self.grade = grade

    def divide(self):
        return self.numerator / self.denominator

    def fuse(self):
        if isinstance(self.numerator, XVar):
            self.numerator.frac(self.denominator)
            return self.numerator


# Clase donde se creará la ecuación
class Equation:

    def __init__(self, level: int, grade: int, result: int):
        self.grade = grade
        self.result = result
        self.level = level

        self.left: list = [XVar(1, 1)]
        self.right: list = [result]

    def multiplyAndUpdate(self, num: int):
        counter = 0
        for item in self.left:
            if isinstance(item, int):
                self.left[counter] = item * num
            elif isinstance(item, XVar):
                item.multiply(num)
            counter += 1

        counter = 0

        for item in self.right:
            if isinstance(item, int):
                self.right[counter] = item * num
            elif isinstance(item, XVar):
                item.multiply(num)
            counter += 1

    def sumAndUpdate(self, num: int, unite: bool = False):
        if unite:
            counter = 0
            found = False
            for item in self.left:
                if isinstance(item, int):
                    self.left[counter] = item + num
                    found = True
                    break
                counter += 1
            if not found:
                self.left.append(num)

            counter = 0
            found = False
            for item in self.right:
                if isinstance(item, int):
                    self.right[counter] = item + num
                    found = True
                    break
                counter += 1
            if not found:
                self.right.append(num)
        else:
            self.left.append(num)
            self.right.append(num)

    def subtractAndUpdate(self, num: int, unite: bool = False):
        if unite:
            counter = 0
            found = False
            for item in self.left:
                if isinstance(item, int):
                    self.left[counter] = item - num
                    found = True
                    break
                counter += 1
            if not found:
                self.left.append(-num)

            counter = 0
            found = False
            for item in self.right:
                if isinstance(item, int):
                    self.right[counter] = item - num
                    found = True
                    break
                counter += 1
            if not found:
                self.right.append(-num)
        else:
            self.left.append(-num)
            self.right.append(-num)

    def scramble(self):
        counter = 0
        while counter < 10:
            if random.randint(0, 1) == 0:
                try:
                    item = random.choice(self.left)
                except IndexError:
                    continue

                self.right.append(-item)
                self.left.remove(item)
            else:
                try:
                    item = random.choice(self.right)
                except IndexError:
                    continue

                self.left.append(-item)
                self.right.remove(item)

            counter += 1

    def randomEvent(self):
        match random.randint(0, 3):
            case 0:
                self.sumAndUpdate(random.randint(1, 9), True if random.randint(0, 1) == 1 else False)
            case 1:
                self.subtractAndUpdate(random.randint(1, 9), True if random.randint(0, 1) == 1 else False)
            case 2:
                self.multiplyAndUpdate(random.randint(1, 9))
            case 3:
                self.scramble()

    def __str__(self):
        text = ""
        counter = 0
        for item in self.left:
            if counter == 0:
                if isinstance(item, int):
                    text += f"- {abs(item)}" if item < 0 else f"{item}"
                elif isinstance(item, XVar):
                    text += f"- {item.__str__(True)}" if item.multiplier < 0 else f"{item.__str__(True)}"
            else:
                if isinstance(item, int):
                    text += f" - {abs(item)}" if item < 0 else f" + {item}"
                elif isinstance(item, XVar):
                    text += f" - {item}" if item.multiplier < 0 else f" + {item}"
            counter += 1

        text += " ="
        counter = 0
        for item in self.right:
            if isinstance(item, int):
                text += f" - {abs(item)}" if item < 0 else f" + {item}"
            elif isinstance(item, XVar):
                text += f" - {item}" if item.multiplier < 0 else f" + {item}"
            counter += 1

        return text


# Clase encargada de gestionar los ejercicios y el nivel de dificultad de los mismos
class Main:

    def __init__(self, quantity: int, level: int):
        self.quantity = quantity
        self.level = level

        for i in range(100):
            self.eq = Equation(level, 1, random.randint(0, 9))
            for j in range(15):
                self.eq.randomEvent()
            print(self.eq)


m = Main(3, 1)

