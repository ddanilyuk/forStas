import math
import tkinter as tk
from lab_2.figure import Figure as figure


def main():
    window = tk.Tk()
    window.title("Lab 2")

    # VARIABLES
    screenSize = (700, 700)  # (width, height)
    canvas = tk.Canvas(window, width=screenSize[0], height=screenSize[1])

    # PARAMETERS :
    density = 1 / 2
    numberOfSpiralTurns = 30

    # turning point ( 0 - centre; 1 - the last point of the spiral; 2 - other point)
    turnPoint = 2

    # geometric model (model = 1)
    # ornament        (model = 2)
    # moire           (model = 3)

    # EDIT THIS VARIABLE !!!!!!
    model = 1

    if model == 1:
        mdl = figure(density, numberOfSpiralTurns, (200, 200))
        mdl.createFigure(canvas, 0, "darkslateblue")

    elif model == 2:
        n = 4

        mdl1 = figure(density, numberOfSpiralTurns, (350, 350))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl1.createFigure(canvas, angle, "palevioletred", turnPoint=turnPoint)

    elif model == 3:
        n = 25

        mdl = figure(density, numberOfSpiralTurns, (230, 230))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl.createFigure(canvas, angle, "Navy Blue", turnPoint=turnPoint)

    window.mainloop()


if __name__ == '__main__':
    main()
