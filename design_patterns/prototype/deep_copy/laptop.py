from abs_computer import AbsComputer
from abs_prototype import AbsPrototype
import copy


class Laptop(AbsComputer, AbsPrototype):
    def __init__(self, model, processor, memory, harddrive, graphics, screen):
        self.model = model
        self.processor = processor
        self.memory = memory
        self.harddrive = harddrive
        self.graphics = graphics
        self.screen = screen

    def display(self):
        print(f"Custom computer: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory}")
        print(f"Hard drive: {self.harddrive}")
        print(f"Graphics: {self.graphics}")
        print(f"Screen: {self.screen}")

    def clone(self):
        return copy.copy(self)
