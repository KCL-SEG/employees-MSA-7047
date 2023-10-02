class Employee:
    def __init__(self, name):
        self.name = name
        self.pay_components = []

    def get_pay(self):
        total_pay = sum(component.calculate() for component in self.pay_components)
        return total_pay

    def __str__(self):
        components_info = " and ".join([str(component) for component in self.pay_components])
        return f"{self.name} works {components_info}. Their total pay is {self.get_pay()}."


class MonthlySalary:
    def __init__(self, salary):
        self.salary = salary

    def calculate(self):
        return self.salary

    def __str__(self):
        return f"on a monthly salary of {self.salary}"


class HourlyContract:
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"


class Commission:
    def __init__(self, commission_count, commission_rate):
        self.commission_count = commission_count
        self.commission_rate = commission_rate

    def calculate(self):
        return self.commission_count * self.commission_rate

    def __str__(self):
        if self.commission_count == 1:
            return f"and receives a bonus commission of {self.commission_rate}"
        else:
            return f"and receives a commission for {self.commission_count} contract(s) at {self.commission_rate}/contract"


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie')
billie.pay_components.append(MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie')
charlie.pay_components.append(HourlyContract(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee')
renee.pay_components.append(MonthlySalary(3000))
renee.pay_components.append(Commission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan')
jan.pay_components.append(HourlyContract(150, 25))
jan.pay_components.append(Commission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie')
robbie.pay_components.append(MonthlySalary(2000))
robbie.pay_components.append(Commission(1, 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel')
ariel.pay_components.append(HourlyContract(120, 30))
ariel.pay_components.append(Commission(1, 600))

# Test cases
print(str(billie))  # Output should match the specified format
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))

