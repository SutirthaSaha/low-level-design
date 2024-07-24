from enum import Enum


class Status(Enum):
    OFF = "Off"
    ON = "On"


class ElectricSystem:
    def __init__(self):
        self.voltage = 0
        self.status = Status.OFF

    def set_voltage(self, voltage):
        if self.status == Status.ON:
            self.voltage = voltage
        else:
            raise Exception("The electric system is not on")

    def turn_on(self):
        self.status = Status.ON
        print("Turn on electric system")

    def turn_off(self):
        self.voltage = 0
        self.status = Status.OFF
        print("Turn off electric system")


class PlumbingSystem:
    def __init__(self):
        self.pressure = 0
        self.status = Status.OFF

    def set_pressure(self, pressure):
        if self.status == Status.ON:
            self.pressure = pressure
        else:
            raise Exception("The plumbing system is not on")

    def turn_on(self):
        self.status = Status.ON
        print("Turn on plumbing system")

    def turn_off(self):
        self.pressure = 0
        self.status = Status.OFF
        print("Turn off plumbing system")


class HousingSystem:
    def __init__(self):
        self.plumbing_system = PlumbingSystem()
        self.electric_system = ElectricSystem()

    def turn_on(self):
        self.electric_system.turn_on()
        self.electric_system.set_voltage(220)
        self.plumbing_system.turn_on()
        self.plumbing_system.set_pressure(100)

    def turn_off(self):
        self.electric_system.turn_off()
        self.plumbing_system.turn_off()


if __name__ == '__main__':
    housing_system = HousingSystem()
    # housing system acts as the facade and a single function call can take care of all the complex functions
    housing_system.turn_on()
    housing_system.turn_off()
