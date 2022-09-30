#write the Dependency Inversion program (from Arjan Codes)
class LightBulb:
    def turn_on(self):
        print(f"LightBulb: turned on...")

    def turn_off(self):
        print(f"LightBulb: turned off...")

class ElectricPowerSwitcher:
    l: LightBulb
    on: bool

    def __init__(self, l, on):
        self.l = l
        self.on = on
    
    def press(self):
        if self.on:
            self.l.turn_on()
            self.on = False
        else:
            self.l.turn_off()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitcher(l, False)
switch.press()
switch.press()
