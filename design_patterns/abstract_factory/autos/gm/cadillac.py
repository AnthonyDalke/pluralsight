from autos.abs_auto import AbsAuto


class CadillacCTS(AbsAuto):
    def start(self):
        print("Cadillac CTS running smoothly.")

    def stop(self):
        print("Cadillac CTS shutting down.")
