# Incógnita de las ecuaciones
import random


class XVar:

    def __init__(self, multiplier: int, grade: int):
        self.multiplier = multiplier
        self.grade = grade

    def multiply(self, num: int):
        self.multiplier *= num

    def __str__(self):
        return (f"{abs(self.multiplier)}x^{self.grade} " if self.grade != 1 else f"{abs(self.multiplier)}x ") if self.multiplier != 1 else (f"x^{self.grade} " if self.grade != 1 else f"x ")


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
        while counter < 3:
            mixList: list = self.left + self.right
            random.shuffle(mixList)

            self.left.clear()
            self.right.clear()

            while len(mixList) > 0:
                item = random.choice(mixList)
                if random.randint(0, 2) == 0:
                    self.left.append(item)
                else:
                    self.right.append(item)
                mixList.remove(item)

            counter += 1

    def randomEvent(self):
        match random.randint(0, 4):
            case 0:
                self.sumAndUpdate(random.randint(0, 10), True if random.randint(0, 2) == 1 else False)
            case 1:
                self.subtractAndUpdate(random.randint(0, 10), True if random.randint(0, 2) == 1 else False)
            case 2:
                self.multiplyAndUpdate(random.randint(0, 10))
            case 3:
                self.scramble()

    def __str__(self):
        text = ""
        counter = 0
        for item in self.left:
            if counter == 0:
                if isinstance(item, int):
                    text += f"- {abs(item)} " if item < 0 else f"{item} "
                elif isinstance(item, XVar):
                    text += f"- {item} " if item.multiplier < 0 else f"{item} "
            else:
                if isinstance(item, int):
                    text += f"- {abs(item)} " if item < 0 else f"+ {item} "
                elif isinstance(item, XVar):
                    text += f"- {item} " if item.multiplier < 0 else f"+ {item} "
            counter += 1

        text += "= "
        counter = 0
        for item in self.right:
            if counter == 0:
                if isinstance(item, int):
                    text += f"- {abs(item)} " if item < 0 else f"{item} "
                elif isinstance(item, XVar):
                    text += f"- {item} " if item.multiplier < 0 else f"{item} "
            else:
                if isinstance(item, int):
                    text += f"- {abs(item)} " if item < 0 else f"+ {item} "
                elif isinstance(item, XVar):
                    text += f"- {item} " if item.multiplier < 0 else f"+ {item} "
            counter += 1

        return text


# Clase encargada de gestionar los ejercicios y el nivel de dificultad de los mismos
class Main:

    def __init__(self, quantity: int, level: int):
        self.quantity = quantity
        self.level = level
        self.eq = Equation(level, 1, 5)
        for i in range(10):
            self.eq.randomEvent()
        print(self.eq)


m = Main(3, 1)
