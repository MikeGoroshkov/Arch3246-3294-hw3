import zope.interface
from classes.Car import Car
from classes.IReFueling import IReFueling

@zope.interface.implementer(IReFueling)
class PickUp(Car):
    __load_capacity = 0

    def __init__(self, name, model, color, body_type, number_wheels, fuel, gear_box, engine_cap, load_capacity):
        super().__init__(name, model, color, body_type, number_wheels, fuel, gear_box, engine_cap)
        self.__load_capacity = load_capacity

    def gear_shift(self, int_arg):
        return -int_arg

    def fuel(self):
        pass

    def wip_windshield(self):
        pass

    def wip_headlight(self):
        pass

    def wip_mirrors(self):
        pass