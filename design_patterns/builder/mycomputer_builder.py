from abs_builder import AbsBuilder


class MyComputerBuilder(AbsBuilder):
    def get_case(self):
        self._computer.case = "Coolermaster"

    def build_mainboard(self):
        self._computer.mainboard = "MSI"
        self._computer.cpu = "Intel Core i9"
        self._computer.memory = "2 x 16GB"

    def install_mainboard(self):
        pass

    def install_harddrive(self):
        self._computer.harddrive = "SSD"

    def install_videocard(self):
        self._computer.videocard = "GeForce GTX"
