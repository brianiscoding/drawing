import digitalio
import time
import pwmio


class Controller:
    def __init__(self, M1, M2, DELAY, PEN, BUTTON):
        self.M1 = M1
        self.M2 = M2
        self.DELAY = DELAY
        self.BUTTON = digitalio.DigitalInOut(BUTTON)
        self.BUTTON.direction = digitalio.Direction.INPUT

        self.PEN = pwmio.PWMOut(PEN, duty_cycle=8000, frequency=100)
        self.pen_is(0)

        for r2 in [100, -100]:
            time.sleep(2)
            while 1:
                if self.BUTTON.value:
                    break
                self.rotate(r1=-100, r2=r2)

    def pen_is(self, a):
        """
        moves pen, turn off power
        """
        self.PEN.duty_cycle = 16000 if a else 8000
        time.sleep(.5)
        self.PEN.duty_cycle = 0

    def rotate(self, r1, r2):
        if r1 < 0:
            self.M1.direction.value = True
            r1 = abs(r1)
        else:
            self.M1.direction.value = False
        if r2 < 0:
            self.M2.direction.value = True
            r2 = abs(r2)
        else:
            self.M2.direction.value = False

        if r1 > r2:
            for _ in range(r2):
                for _ in range(r1 // r2):
                    time.sleep(self.DELAY)
                    self.M1.step.value = not self.M1.step.value
                self.M2.step.value = not self.M2.step.value
            try:
                for _ in range(r1 % r2):
                    time.sleep(self.DELAY)
                    self.M1.step.value = not self.M1.step.value
            except:
                for _ in range(r1):
                    time.sleep(self.DELAY)
                    self.M1.step.value = not self.M1.step.value
        else:
            for _ in range(r1):
                for _ in range(r2 // r1):
                    time.sleep(self.DELAY)
                    self.M2.step.value = not self.M2.step.value
                self.M1.step.value = not self.M1.step.value
            try:
                for _ in range(r2 % r1):
                    time.sleep(self.DELAY)
                    self.M2.step.value = not self.M2.step.value
            except:
                for _ in range(r2):
                    time.sleep(self.DELAY)
                    self.M2.step.value = not self.M2.step.value

    
