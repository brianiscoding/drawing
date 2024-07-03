# from Controller import Controller
# from Motor import Motor
from t import create_rotations_out
from os import listdir, replace
from subprocess import call
# from board import board


def main():
    inf = "graphs.svg"

    inf = input("\nenter input file name: ")
    if inf not in listdir("input"):
        print("file not found. goodbye.\n")
        return
    
    call(["java", "-jar", "lib/svgeq.jar", f"input/{inf}"])
    with open(file="output/equations.txt", mode ="w") as _:
        pass
    replace(src=f"input/{inf.split('.')[0]}-output.txt", dst="output/equations.txt")
    with open(file="output/equations.txt", mode ="a") as f:    
        f.write("\n")

    create_rotations_out(ppa=0.4, scale=10)

    # motor2 = Motor(
    #     direction=board.GP0,
    #     step=board.GP1,
    #     sleep=board.GP2,
    #     reset=board.GP3,
    #     mode_2=board.GP4,
    #     mode_1=board.GP5,
    #     mode_0=board.GP6,
    # )
    # motor1 = Motor(
    #     direction=board.GP8,
    #     step=board.GP9,
    #     sleep=board.GP10,
    #     reset=board.GP11,
    #     mode_2=board.GP12,
    #     mode_1=board.GP13,
    #     mode_0=board.GP14,
    # )
    # controller = Controller(
    #     M1=motor1, M2=motor2, DELAY=0.0008, PEN=board.GP22, BUTTON=board.GP16
    # )
    
    # with open(file="output/rotations.txt" , mode="r") as f:
    #     f = f.readlines()
    # for line in f:
    #     line = line[:-1]
    #     rotations = line.split(" ")
    #     rotation = rotations.split(",")
    #     r1 = int(rotation[0])
    #     r2 = int(rotation[1])
    #     for rotation in line.split(" "):
    #         rotation = rotation.split(",")
    #         r1 = int(rotation[0])
    #         r2 = int(rotation[1])

main()
