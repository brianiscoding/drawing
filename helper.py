from sympy import sympify, Curve, Symbol
from math import dist


def create_line(line, t, ppa, scale):
    line = line.replace("-t", "?")
    line = line.replace("t", "*t")
    line = line.replace("?", "-t")
    line = line.replace("^", "**")
    line = line.replace("(", "*(")
    line = line.split(", ")
    line = Curve((sympify(line[0]), sympify(line[1])), (t, 0, 1))

    fx = line.functions[0]
    fy = line.functions[1]
    ends = [(round(fx.subs(t, i), 4), round(fy.subs(t, i), 4)) for i in range(2)]
    size = int(ppa * dist(ends[0], ends[1])) + 1

    # DELETE
    for end in ends:
        if end[1] > 0 or end[0] < 0:
            return ""

    if 0:
        line = f"({scale*ends[0][0]},{scale*ends[0][1]})\n"
        for i in range(1, size):
            line += f"({scale*round(fx.subs(t, i / size), 4)},{scale*round(fy.subs(t, i / size), 4)})\n"
        line += f"({scale*ends[1][0]},{scale*ends[1][1]})\n"
        return line

    line = f"{scale*ends[0][0]},{-1*scale*ends[0][1]} "
    for i in range(1, size):
        line += f"{scale*round(fx.subs(t, i / size), 4)},{-1*scale*round(fy.subs(t, i / size), 4)} "
    line += f"{scale*ends[1][0]},{-1*scale*ends[1][1]}\n"
    return line


def create_approximations_out(ppa, scale):
    with open(file=f"output/equations.txt", mode="r") as f:
        lines = f.readlines()

    t = Symbol("t")
    with open(file="output/approximations.txt", mode="w") as f:
        for line in lines[:-1]:
            line = line[1:-2]
            f.write(create_line(line=line, t=t, ppa=ppa, scale=scale))
        line = lines[-1]
        line = line[1:-1]
        f.write(create_line(line=line, t=t, ppa=ppa, scale=scale))


def create_rotations_out():
    with open(file="output/approximations.txt", mode="r") as f:
        lines = f.readlines()

    x = 0
    y = 0
    with open(file="output/rotations.txt", mode="w") as f:
        for points in lines:
            points = points[:-1]
            points = points.split(" ")
            for point in points[:-1]:
                point = point.split(",")
                delta_x = float(point[0]) - x
                delta_y = float(point[1]) - y
                x = float(point[0])
                y = float(point[1])
                f.write(
                    f"{round((delta_x + delta_y) / 2**0.5)},{round((delta_x - delta_y) / 2**0.5)} "
                )
            point = points[-1]
            point = point.split(",")
            delta_x = float(point[0]) - x
            delta_y = float(point[1]) - y
            x = float(point[0])
            y = float(point[1])
            f.write(
                f"{round((delta_x + delta_y) / 2**0.5)},{round((delta_x - delta_y) / 2**0.5)}\n"
            )



