from abs_computer import AbsComputer
from abs_prototype import AbsPrototype
import copy


class MainBoard(object):
    manufacturer: str
    model: str

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Tower(AbsComputer, AbsPrototype):
    def __init__(
        self, model, mainboard, processor, memory, harddrive, graphics, monitor
    ):
        self.model = model
        self.mainboard = mainboard
        self.processor = processor
        self.memory = memory
        self.harddrive = harddrive
        self.graphics = graphics
        self.monitor = monitor

    def display(self):
        print(f"Custom computer: {self.model}")
        print(f"Mainboard: {self.mainboard.manufacturer} {self.mainboard.model}")
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory}")
        print(f"Hard drive: {self.harddrive}")
        print(f"Graphics: {self.graphics}")
        print(f"Monitor: {self.monitor if self.monitor else 'None'}")

    def clone(self):
        return copy.deepcopy(self)
