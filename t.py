from sympy import sympify, Curve, Symbol
from math import dist


def create_rotations_out(ppa, scale):
    with open(file=f"output/equations.txt", mode="r") as f:
        lines = f.readlines()

    t = Symbol("t")
    pos = (0, 0)
    with open(file="output/rotations.txt", mode="w") as f:
        f.write("0,0")
        for line in lines:
            line = line[1:-2]
            line = line.replace("-t", "?")
            line = line.replace("t", "*t")
            line = line.replace("?", "-t")
            line = line.replace("^", "**")
            line = line.replace("(", "*(")
            line = line.split(", ")
            line = Curve((sympify(line[0]), sympify(line[1])), (t, 0, 1))

            start = (
                round(scale * line.functions[0].subs(t, 0), 4),
                round(-1 * scale * line.functions[1].subs(t, 0), 4),
            )
            if start[1] < 0 or start[0] < 0:
                continue
            end = (
                round(scale * line.functions[0].subs(t, 1), 4),
                round(-1 * scale * line.functions[1].subs(t, 1), 4),
            )
            if end[1] < 0 or end[0] < 0:
                continue
            size = int(ppa * dist(start, end) / scale) + 1

            if 0:
                f.write(f"({start[0]},{start[1]})\n")
                for i in range(1, size):
                    f.write(
                        f"({round(scale*line.functions[0].subs(t, i / size), 4)},{round(-1*scale*line.functions[1].subs(t, i / size), 4)})\n"
                    )
                f.write(f"({end[0]},{end[1]})\n")
            else:
                if pos == start:
                    f.write(" ")
                else:
                    delta_x = start[0] - pos[0]
                    delta_y = start[1] - pos[1]
                    pos = start
                    f.write(
                        f"\n{round((delta_x + delta_y) / 2**0.5)},{round((delta_x - delta_y) / 2**0.5)} "
                    )
                for i in range(1, size):
                    point = (
                        round(scale * line.functions[0].subs(t, i / size), 4),
                        round(-1 * scale * line.functions[1].subs(t, i / size), 4),
                    )
                    delta_x = point[0] - pos[0]
                    delta_y = point[1] - pos[1]
                    pos = point
                    f.write(
                        f"{round((delta_x + delta_y) / 2**0.5)},{round((delta_x - delta_y) / 2**0.5)} "
                    )
                delta_x = end[0] - pos[0]
                delta_y = end[1] - pos[1]
                pos = end
                f.write(
                    f"{round((delta_x + delta_y) / 2**0.5)},{round((delta_x - delta_y) / 2**0.5)}"
                )
        f.write(" ")
