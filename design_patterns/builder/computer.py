class Computer(object):
    case: str
    mainboard: str
    cpu: str
    memory: str
    harddrive: str
    videocard: str

    def display(self):
        print("Custom computer:\n")
        print(f"Case: {self.case}")
        print(f"Mainboard: {self.mainboard}")
        print(f"CPU: {self.cpu}")
        print(f"Memory: {self.memory}")
        print(f"Hard drive: {self.harddrive}")
        print(f"Video card: {self.videocard}")
