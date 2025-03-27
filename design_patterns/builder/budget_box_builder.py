from abs_builder import AbsBuilder


class BudgetBoxBuilder(AbsBuilder):
    def get_case(self):
        self._computer.case = "Corsair"

    def build_mainboard(self):
        self._computer.mainboard = "Asus"
        self._computer.cpu = "AMD"
        self._computer.memory = "2 x 4GB"

    def install_mainboard(self):
        pass

    def install_harddrive(self):
        self._computer.harddrive = "Seagate"

    def install_videocard(self):
        self._computer.videocard = "Onboard"
