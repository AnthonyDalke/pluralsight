class Employee:
    def __init__(self, name_first, name_last):
        self.fname = name_first
        self.lname = name_last


class SalaryEmployee(Employee):
    def __init__(self, name_first, name_last, salary):
        super().__init__(name_first, name_last)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, name_first, name_last, weekly_hours, hourly_rate):
        super().__init__(name_first, name_last)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, name_first, name_last, salary, sales_count, comm_rate):
        super().__init__(name_first, name_last, salary)
        self.sales_count = sales_count
        self.comm_rate = comm_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_count * self.comm_rate
        return regular_salary + total_commission
