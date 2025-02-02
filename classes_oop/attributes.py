class Employee:
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError(f"Company went bankrupt")
        cls.minimum_wage = new_wage

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee works as a {self.position}, with a salary of {self.salary}."

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f"Minimum wage is {Employee.minimum_wage}.")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

# Test repr function
print(f"\nTesting repr function...")
print(eval(repr(employee1)))

# Test cached property
print(f"\nTesting cached property...")
print(employee1.annual_salary)
employee1.salary = 1000
print(employee1.annual_salary)

# Test dict of class instance
print(f"\nTesting dict of class instance...")
e = Employee("Ji-Soo", 38, "developer", 1000)
Employee.__dict__["increase_salary"](e, 20)
print(e.salary)

# Test default attribute
print(f"\nTesting default attribute...")
print(e.minimum_wage)
print(Employee.minimum_wage)

# Test class attribute
print(f"\nTesting class attribute...")
print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)
