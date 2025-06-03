import random
from elements import XVar, Fraction, randomChoice


# Class which handles all the equation factory
class Equation:

    def __init__(self, quantity: int, level: int, friendlyView: bool = False):
        self.quantity = quantity
        self.level = level
        self.saved: list = []
        self.solution: int

        for i in range(15):
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
        # More coming soon

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
        pass

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

    def randomResult(self):
        if randomChoice():
            f = Fraction(self, [random.randint(1, 50)], [random.randint(1, 50)])
            self.solution = f.simplify()
        else:
            self.solution = random.randint(0, 50)

# m = Main(3, 1)

