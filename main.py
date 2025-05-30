import random
from elements import XVar, Fraction, randomChoice


# Class which handles all the equation factory
class Equation:

    def __init__(self, quantity: int, level: int, friendlyView: bool = False):
        self.quantity = quantity
        self.level = level
        self.saved: list = []

        for i in range(15):
            self.left: list = [XVar(self, 1, 1)]
            self.right: list = []
            self.generate()
            if not friendlyView:
                print(f"{i + 1}. {self}")
        # More coming soon


    def generate(self):
        result = self.randomResult()
        self.right.append(result)
        # More coming soon

    def multiplyAndUpdate(self, num: int | Fraction):
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

    def randomResult(self):
        if randomChoice():
            return Fraction(self, [random.randint(1, 50)], [random.randint(1, 50)])
        else:
            return random.randint(0, 50)

# m = Main(3, 1)

