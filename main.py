import random
from elements import XVar, Fraction, randomChoice


# Class which handles all the equation factory
class Equation:

    def __init__(self, quantity: int, level: int, friendlyView: bool = False):
        self.quantity = quantity
        self.level = level
        self.saved: list = []
        self.solution: int

        for i in range(quantity):
            self.left: list = [XVar(self, 1, 1)]
            self.right: list = []
            self.generate()
            if friendlyView:
                print(f"{i + 1}. {self}")
            else:
                self.saved.append(self.toFunction())
        # More coming soon

    def toFunction(self):
        pass

    def generate(self):
        self.randomResult()
        self.right.append(self.solution)

        for i in range(10):
            if randomChoice():
                num = XVar(self, random.randint(1, 9), 1)
            elif randomChoice():
                num = Fraction(self, [random.randint(1, 9)], [random.randint(1, 9)], 1, 1)
            else:
                num = random.randint(1, 10)
            match random.randint(0, 6):
                case 0:
                    self.multiply(num)
                case 1:
                    self.divide(random.randint(1, 10))
                case 2:
                    self.sum(num)
                case 3:
                    self.subtract(num)
                case 4:
                    self.scramble()

    def multiply(self, num: int | XVar | Fraction):

        counter = 0
        for item in self.left:
            self.left[counter] = item * num
            counter += 1

        counter = 0
        for item in self.right:
            self.right[counter] = item * num
            counter += 1

    def divide(self, num: int):

        counter = 0
        for item in self.left:
            self.left[counter] = item / num
            counter += 1

        counter = 0
        for item in self.right:
            self.right[counter] = item / num
            counter += 1

    def sum(self, num: int | XVar | Fraction):
        self.left.append(num)
        self.right.append(num)

    def subtract(self, num: int | XVar | Fraction):
        self.left.append(-num)
        self.right.append(-num)

    def scramble(self):

        for i in range(10):
            if randomChoice():
                if len(self.left) > 0:
                    item = random.choice(self.left)
                    self.right.append(-item)
                    self.left.remove(item)
                else:
                    item = random.choice(self.right)
                    self.left.append(-item)
                    self.right.remove(item)
            else:
                if len(self.right) > 0:
                    item = random.choice(self.right)
                    self.left.append(-item)
                    self.right.remove(item)
                else:
                    item = random.choice(self.left)
                    self.right.append(-item)
                    self.left.remove(item)

    def __str__(self):
        text = ""
        counter = 0
        for item in self.left:

            if counter == 0:
                text += f"- {abs(item) if isinstance(item, int) else item}" if item < 0 else f"{item}"
            else:
                text += f" - {abs(item) if isinstance(item, int) else item}" if item < 0 else f" + {item}"

            counter += 1

        text += " ="
        counter = 0
        for item in self.right:
            if counter == 0:
                text += f" - {abs(item) if isinstance(item, int) else item}" if item < 0 else f" {item}"
            else:
                text += f" - {abs(item) if isinstance(item, int) else item}" if item < 0 else f" + {item}"
            counter += 1

        return text

    def randomResult(self):
        if randomChoice():
            f = Fraction(self, [random.randint(1, 50)], [random.randint(1, 50)])
            self.solution = f.simplify()
        else:
            self.solution = random.randint(0, 50)

e = Equation(10, 1, True)