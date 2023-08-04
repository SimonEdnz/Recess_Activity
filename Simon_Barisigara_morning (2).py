# Calculate and display the area of a rectangle and perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

rectangle = Rectangle(length, width)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Area:", area)
print("Perimeter:", perimeter)

""" Calculate and display the employee bonuses(15%) of salary
(use object's employee1 :150000 , employee2 :230000"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.15


employee1 = Employee(150000)
employee2 = Employee(230000)

bonus1 = employee1.calculate_bonus()
bonus2 = employee2.calculate_bonus()

print("Employee 1 Bonus:", bonus1)
print("Employee 2 Bonus:", bonus2)


# To convert temperature from Celsius to Fahrenheit, you can use the following formula:
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


celsius = 37

converter = TemperatureConverter(celsius)
fahrenheit = converter.celsius_to_fahrenheit()

print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

"""
ENCAPSULATION
key main goals of encapsulation are,
1.to hide the implementation details of an object
 2. to protect the object from changes
 3. to protect the object from external changes
 4. code organization and modularity
EXERCISE
Show encapsulation with employee information to give a pay incrementation 
 (salary with employee information to a new_salary) eg from 85000 to 100000"""

class Employee:
    def __init__(self, name, id, salary):
        self._name = name
        self._id = id
        self._salary = salary

    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._id

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary


# Create an employee object
employee = Employee("Simon Bin", 345326, 850000)

# Display the employee information
print("Employee Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Salary:", employee.get_salary())

# Update the salary with a pay increment
new_salary = 1000000
employee.set_salary(new_salary)
print("\nSalary updated to:", employee.get_salary())

# example 4 encapsulation with bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance


# Create a bank account object
account = BankAccount("34765833", 165000)

# Try to access the account number directly
print("Account Number:", account._account_number)

# Access the balance using the get_balance() method
print("Balance:", account.get_balance())

# Make a deposit
account.deposit(2000)

# Withdraw an amount
account.withdraw(3000)

# Check the updated balance
print("Updated Balance:", account.get_balance())

"""
class Car:
    def __init__(self, make, model, Year):
        self.make = make
        self.model = model
        self.Year = year

    def start_engine(self):
        print("engine started")

    def stop_engine(self):
        print("engine stopped")


my_car = Car("bmw", "vxm", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()




# example 2
class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self. year = year

    def show_details(self):
        print("my name is ", self.name)
        print("i do ", self.course)
        print("year is ", self.year)


std = Student("simon", "bsse", "2020")
std.show_details()

EMPLOYEE BONUS
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name, "earns",self.salary)
    def calculate(self):
        if self.salary > 150000:
            print(self.salary*0.15)
        else:
            print(self.salary)
emp1 = Employee("Simon",150000)
emp1.display()
emp1.calculate()
emp1=Employee("Bin",230000)
emp1.display()
emp1.calculate()

"""
