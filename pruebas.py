
class XVad:

    def __init__(self, mult: int):
        self.mult = mult

    def __mul__(self, other):
        self.mult = other * self.mult

        return self

    def __int__(self):
        return self.mult

    def __str__(self):
        return f"{self.mult}X"


c = XVad(2)

d = XVad(3)

print(type(c) == type(d))