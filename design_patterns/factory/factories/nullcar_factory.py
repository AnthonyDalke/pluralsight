from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullFactory(AbsFactory):
    def create_auto(self):
        self.nullcar = nullcar = NullCar(carname="does not exist")
        return nullcar
