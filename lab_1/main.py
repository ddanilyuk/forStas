import tkinter as tk
import math
from lab_1.romb import Romb as model


def main():
    window = tk.Tk()
    window.title("Lab 1")

    screenSize = (900, 900)  # (width, height)
    canvas = tk.Canvas(window, width=screenSize[0], height=screenSize[1])

    size = 1

    # Romb 1
    vd_1 = 175 * size  # vertical diagonal 1
    hd_1 = 400 * size  # horizontal diagonal 1

    # Romb 2
    vd_2 = 160 * size  # vertical diagonal 2
    hd_2 = 160 * size  # horizontal diagonal 2

    # coordinates of the start point
    x = 200
    y = 300

    # geometric model (modelN = 1)
    # ornament        (modelN = 2)
    # moire           (modelN = 3)

    # EDIT THIS VARIABLE !!!!!!
    modelN = 1

    if modelN == 1:

        mdl = model(hd_1, vd_1, (x, y))
        mdl.createFigure(canvas, 0, "darkslateblue")

    elif modelN == 2:
        n = 5
        m = 5

        mdl1 = model(hd_1, vd_1, (x, y))
        mld1Center = mdl1.get_center_coord()
        mdl2 = model(hd_2, vd_2, ((mld1Center[0] - hd_2 / 2) / 1, (mld1Center[1] - vd_2 / 2) / 1))

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl1.createFigure(canvas, angle, "darkslateblue")

        for angle in [math.pi / m * i for i in range(-m, m)]:
            mdl2.createFigure(canvas, angle, "palevioletred")

    elif modelN == 3:
        n = 40
        m = 50

        mdl1 = model(hd_1, vd_1, (x, y))
        mld1Center = mdl1.get_center_coord()
        mdl2 = model(hd_2, vd_2, ((mld1Center[0] - hd_2 / 2) / 1, (mld1Center[1] - vd_2 / 2) / 1))

        for angle in [math.pi / m * i for i in range(-m, m)]:
            mdl2.createFigure(canvas, angle, "palevioletred")

        for angle in [math.pi / n * i for i in range(-n, n)]:
            mdl1.createFigure(canvas, angle, "darkslateblue")

    window.mainloop()


if __name__ == '__main__':
    main()
