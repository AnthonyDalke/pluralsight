from .abs_decorator import AbsDecorator


class I4(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ", I4"

    @property
    def cost(self):
        return self.car.cost + 500.00
