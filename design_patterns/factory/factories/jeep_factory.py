from .abs_factory import AbsFactory
from autos.jeepsahara import JeepSahara


class JeepFactory(AbsFactory):
    def create_auto(self):
        self.jeep = jeep = JeepSahara()
        jeep.name = "Jeep Sahara"
        return jeep
