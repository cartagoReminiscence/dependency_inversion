#write the Dependency Inversion program (from Arjan Codes)

from abc import ABC, abstractmethod

class Switch(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switch):
    def turn_on(self):
        print(f"LightBulb: turned on...")

    def turn_off(self):
        print(f"LightBulb: turned off...")

class ElectricPowerSwitcher:
    s: Switch
    on: bool

    def __init__(self, s, on):
        self.s = s
        self.on = on
    
    def press(self):
        if self.on:
            self.s.turn_on()
            self.on = False
        else:
            self.s.turn_off()
            self.on = True

s = LightBulb()
switch = ElectricPowerSwitcher(s, False)
switch.press()
switch.press()
