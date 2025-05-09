import abc
from computer import Computer


class AbsBuilder(abc.ABC):
    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def install_harddrive(self):
        pass

    @abc.abstractmethod
    def install_videocard(self):
        pass
