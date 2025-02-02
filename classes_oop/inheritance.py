from datetime import date


class Employee:
    minimum_wage = 1000

    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)


class Tester(Employee):
    def run_tests(self):
        print(f"Testing initiated by {self.name}...")
        print(f"Tests completed!")


class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, "__slots__")


class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework",)

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000, "Flask")

# Test method inheritance
employee1.increase_salary(20)
employee2.increase_salary(20, 30)
print(employee1.salary)
print(employee2.salary)

# Test attribute addition
print(employee2.name)
print(employee2.framework)

# Test mixin class
print(employee2.has_slots())
print(Developer.__mro__)

# Test factory function
print(f"\nTesting factory function...")
e = Employee.new_employee("Mary", date(1991, 8, 12))
print(e.name)
print(e.age)
print(e.salary)
