from .abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print("Chevy Volt started")

    def stop(self):
        print("Chevy Volt stopped")
