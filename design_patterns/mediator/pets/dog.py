from .abs_pet import AbsPet


class Dog(AbsPet):
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def wants_walk(self):
        if self.mediator.is_cat_asleep():
            print(f"Walk {self.name}")
        else:
            print(f"Wake up {self.name}")
            self.mediator.wake_up_cat()
