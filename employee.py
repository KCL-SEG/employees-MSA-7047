from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class MonthlyEmployee(Employee):
    def __init__(self, name, monthly_salary, commission=None):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.commission = commission

    def get_pay(self):
        total_pay = self.monthly_salary
        if self.commission:
            total_pay += self.commission.get_pay()
        return total_pay

    def __str__(self):
        commission_info = self.commission.get_string() if self.commission else ""
        return f"{self.name} works on a monthly salary of {self.monthly_salary}{commission_info}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_pay, hours_worked, commission=None):
        super().__init__(name)
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
        self.commission = commission

    def get_pay(self):
        total_pay = self.hourly_pay * self.hours_worked
        if self.commission:
            total_pay += self.commission.get_pay()
        return total_pay

    def __str__(self):
        commission_info = self.commission.get_string() if self.commission else ""
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_pay}/hour{commission_info}. Their total pay is {self.get_pay()}."

class Commission(ABC):
    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def get_pay(self):
        pass

class BonusCommission(Commission):
    def __init__(self, commission_pay):
        super().__init__()
        self.commission_pay = commission_pay

    def get_string(self):
        return f" and receives a bonus commission of {self.commission_pay}"

    def get_pay(self):
        return self.commission_pay

class ContractCommission(Commission):
    def __init__(self, commission_pay, commission_number):
        super().__init__()
        self.commission_pay = commission_pay
        self.commission_number = commission_number

    def get_string(self):
        return f" and receives a commission for {self.commission_number} contract(s) at {self.commission_pay}/contract"

    def get_pay(self):
        return self.commission_pay * self.commission_number

# Examples
billie = MonthlyEmployee('Billie', 4000)
print(str(billie))

charlie = HourlyEmployee('Charlie', 25, 100)
print(str(charlie))

renee = MonthlyEmployee('Renee', 3000, ContractCommission(200, 4))
print(str(renee))

jan = HourlyEmployee('Jan', 25, 150, ContractCommission(220, 3))
print(str(jan))

robbie = MonthlyEmployee('Robbie', 2000, BonusCommission(1500))
print(str(robbie))

ariel = HourlyEmployee('Ariel', 30, 120, BonusCommission(600))
print(str(ariel))
