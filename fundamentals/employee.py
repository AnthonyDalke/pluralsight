class Employee:
    def __init__(self, name_first, name_last, salary):
        self.fname = name_first
        self.lname = name_last
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52
