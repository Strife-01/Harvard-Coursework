class Point():
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY

    @property
    def coordX(self):
        return self._coordX

    @coordX.setter
    def coordX(self, coordX):
        if coordX < 0:
            raise ValueError("Value less than 0")
        self._coordX = coordX

    @property
    def coordY(self):
        return self._coordY

    @coordY.setter
    def coordY(self, coordY):
        self._coordY = coordY

    def __str__(self):
        return f"X = {self.coordX}, Y = {self.coordY}"


p = Point(10.0, 20.0)

p.coordX = -1

print(p)
