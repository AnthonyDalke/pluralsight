import random
from .abs_pet import AbsPet


class Fish(AbsPet):
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def needs_food(self):
        if self.mediator.is_morning():
            print(f"Feed {self.name}")
        else:
            print(f"{self.name} doesn't feel hungry")

    def is_alive(self):
        return random.randint(0, 1)
