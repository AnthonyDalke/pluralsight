from autos.abs_auto import AbsAuto


class ChevySpark(AbsAuto):
    def start(self):
        print("Chevy Spark running cheaply.")

    def stop(self):
        print("Chevy Spark shutting down.")
