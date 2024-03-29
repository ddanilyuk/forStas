import math
import numpy


class Figure:

    def __init__(self, density: float, parameterN: int, centerPoint: tuple):
        self.density = density
        self.sizeN = parameterN
        self.centerPoint = centerPoint

    def getXY(self) -> list:
        allPoints: list = []
        for t in numpy.arange(0.0, self.sizeN * math.pi, 0.1):
            x = t * math.sin(t * self.density)
            y = t * math.cos(t * self.density)
            x += self.centerPoint[0]
            y += self.centerPoint[1]

            allPoints.append((x, y))

        return allPoints

    def turning_point_end(self) -> tuple:
        t = self.sizeN * math.pi
        x = t * math.sin(t * self.density)
        y = t * math.cos(t * self.density)
        x += self.centerPoint[0]
        y += self.centerPoint[1]
        return x, y

    def turning_point(self) -> tuple:
        x = self.centerPoint[0] + 75
        y = self.centerPoint[1] + 75
        return x, y

    def turning_point_center(self) -> tuple:
        x = self.centerPoint[0]
        y = self.centerPoint[1]
        return x, y

    def _transform(self, x: tuple, y: tuple, turnPoint: tuple, angle: float) -> tuple:
        x -= turnPoint[0]
        y -= turnPoint[1]

        temp_x = x * numpy.cos(angle) - y * numpy.sin(angle)
        temp_y = x * numpy.sin(angle) + y * numpy.cos(angle)

        return temp_x + turnPoint[0], temp_y + turnPoint[1]

    def rotate(self, angle: float, turnPoint: int = 0) -> list:
        turnedPoint = (self.turning_point_center(), self.turning_point_end(), self.turning_point())[turnPoint]

        rotated_coordinates = [
            self._transform(x, y, turnedPoint, angle) for x, y in self.getXY()
        ]

        return rotated_coordinates

    def createFigure(self, canvas, angle: float, color: str = "Black", turnPoint: int = 0):
        m = self.rotate(angle, turnPoint=turnPoint)

        for i in range(len(m) - 1):
            canvas.create_line(m[i][0], m[i][1], m[i + 1][0], m[i + 1][1], fill=color)

        canvas.pack()
