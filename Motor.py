import digitalio


class Motor:
    def __init__(self, direction, step, sleep, reset, mode_0, mode_1, mode_2):
        self.direction = digitalio.DigitalInOut(direction)
        self.step = digitalio.DigitalInOut(step)
        self.sleep = digitalio.DigitalInOut(sleep)
        self.reset = digitalio.DigitalInOut(reset)
        self.mode_2 = digitalio.DigitalInOut(mode_2)
        self.mode_1 = digitalio.DigitalInOut(mode_1)
        self.mode_0 = digitalio.DigitalInOut(mode_0)

        self.direction.direction = digitalio.Direction.OUTPUT
        self.step.direction = digitalio.Direction.OUTPUT
        self.sleep.direction = digitalio.Direction.OUTPUT
        self.reset.direction = digitalio.Direction.OUTPUT
        self.mode_0.direction = digitalio.Direction.OUTPUT
        self.mode_1.direction = digitalio.Direction.OUTPUT
        self.mode_2.direction = digitalio.Direction.OUTPUT

        self.sleep.value = True
        self.reset.value = True
        self.mode_2.value = False
        self.mode_1.value = False
        self.mode_0.value = True
