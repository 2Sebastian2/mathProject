
class XVad:

    def __init__(self, mult: int):
        self.mult = mult

    def __mul__(self, other):
        self.mult = other * self.mult
        if self.mult
        return self

    def __str__(self):
        return f"{self.mult}X"


c = XVad(2)

d = XVad(3)

c *= d

print(c)