# Inheritance

class Animal:
    def __init__(self, fname):
        self.firstname = fname

    def eat(self):
        print(f"{self.firstname} is eating")


class Dog(Animal):
    # Use the pass keyword when you do not want to add any other properties or methods to the class
    def bark(self):
        print(f"{self.firstname} is a dog")


class Cat(Animal):
    def meow(self):
        print(f"{self.firstname} is a cat")


# objects
animal = Animal("generic animal")
dg1 = Dog("spot")
ct1 = Cat("pusi")

animal.eat()
ct1.meow()
dg1.bark()
dg1.eat()


# example2
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print("brand is", self.brand)
        print("color is", self.color)

    def move(self):
        print("my vehicle is moving....")


class Car(Vehicle):

    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels=num_wheels
    def wheel(self):
        print("wheels is", self.num_wheels)
    def honk(self):
        print("honking")


mycar = Car("toyota", "red", 4)
print("brand:", mycar.brand)
mycar.color = "blue"
mycar.honk()
mycar.wheel()

# exercise1 demonstate using the inheritence to calculate the area and
# perimeter of a circle and rectangle respectively(shape:circle)
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Usage example
circle = Circle(5)
print("Circle Area:", circle.area())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())


# multiple inheritence
class Animal:
    def __init__(self, name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species= species

    def dispay(self):
        print(f"species :{self.species} ")
        print(f"name :{self.name} ")
my_bird=Bird("pigeon","bird")
my_bird.eat()
my_bird.fly()
my_bird.dispay()

# method overriding
class Animal:
    def make_sound(self):
        print("animal is making a sound")
class Dog(Animal):
    def make_sound(self):
        print("dog is barking")
class Cat(Animal):
    def make_sound(self):
        print("cat is meowing")
def make_animal_sound(animal):
    animal.make_sound()
# create objects
animal = Animal()
dog=Dog()
cat= Cat()

# we use make_animal_sound function to override make sound
make_animal_sound(animal)

make_animal_sound(dog)

make_animal_sound(cat)

# polymorphism
""" allows u to write code that can work with different objects
>method overriding occurs when a derived class provides its own implementation of a method 
that is already defined in its base class.
>method overloading allows a class to have multiple methods with the same name but 
different parameters
"""
# example
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2
    def calculate_circumference(self):
        return 2*3.14*self.radius
rectangle = Rectangle(5, 3)
circle = Circle(7)

print("area of rectangle:", rectangle.calculate_area())
print("area of a circle:", circle.calculate_area())
print("circumference of a circle: ", circle.calculate_circumference())


class Calculator:
    def add(self, x, y):
        return x+y
    def add(self, x, y, c):
        return x+y+c
calc=Calculator()
print(calc.add(3, 4 ,1))
print(calc.add(6, 7, 8))

# ABSTRACTION

# allows u to focus on essential features and hide them from unnecessary details.

# example
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("starting the car")
    def stop(self):
        print("stopping the car")
class Truck(Vehicle):
    def start(self):
        print("starting the truck")

    def stop(self):
        print("stopping the truck")
car = Car()
truck = Truck()

# start method
car.start()
truck.start()
# stop method
car.stop()
truck.stop()

# exercise 2 demonstrate abstraction using calculating area of a circle and rectangle
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Usage example
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

# EXERCISE

# assignment 1 for day 5 create a receipt printing program with a  GUI interface .
# a more advanced detail earns u more points
import tkinter as tk

class Receipt:
    def __init__(self, customer, items, prices, quantities):
        self.customer = customer
        self.items = items
        self.prices = prices
        self.quantities = quantities

    def print_receipt(self):
        raise NotImplementedError("Subclasses must implement print_receipt()")

    def display(self):
        receipt = self.get_receipt_text()
        print(receipt)

    def get_receipt_text(self):
        raise NotImplementedError("Subclasses must implement get_receipt_text()")


class TextReceipt(Receipt):
    def print_receipt(self):
        receipt = self.get_receipt_text()
        print(receipt)

    def get_receipt_text(self):
        receipt = f"Receipt for: {self.customer}\n\n"
        receipt += "Items:\n"
        receipt += f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}\n"
        receipt += '-' * 55 + '\n'
        for item, price, quantity in zip(self.items, self.prices, self.quantities):
            subtotal = price * quantity
            receipt += f"{item.strip():<20} ${price:<10.2f} {quantity:<10} ${subtotal:<10.2f}\n"
        receipt += '-' * 55 + '\n'
        receipt += f"{'Total:':<40} ${sum([price * quantity for price, quantity in zip(self.prices, self.quantities)]):.2f}"
        return receipt


class GUIReceipt(Receipt):
    def __init__(self, customer, items, prices, quantities, master):
        super().__init__(customer, items, prices, quantities)
        self.master = master

        self.label_receipt = tk.Label(master, text="")
        self.label_receipt.pack()

    def print_receipt(self):
        receipt = self.get_receipt_text()
        self.label_receipt.config(text=receipt)

    def get_receipt_text(self):
        receipt = f"Receipt for: {self.customer}\n\n"
        receipt += "Items:\n"
        receipt += f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Subtotal':<10}\n"
        receipt += '-' * 55 + '\n'
        for item, price, quantity in zip(self.items, self.prices, self.quantities):
            subtotal = price * quantity
            receipt += f"{item.strip():<20} ${price:<10.2f} {quantity:<10} ${subtotal:<10.2f}\n"
        receipt += '-' * 55 + '\n'
        receipt += f"{'Total:':<40} ${sum([price * quantity for price, quantity in zip(self.prices, self.quantities)]):.2f}"
        return receipt


class ReceiptPrintingApp:
    def __init__(self, master):
        self.master = master
        master.title("Receipt")

        # Create input labels and entry fields
        self.label_customer = tk.Label(master, text="Customer_name:")
        self.label_customer.pack()
        self.entry_customer = tk.Entry(master)
        self.entry_customer.pack()

        self.label_items = tk.Label(master, text="Items (separated by |):")
        self.label_items.pack()
        self.entry_items = tk.Entry(master)
        self.entry_items.pack()

        self.label_prices = tk.Label(master, text="Prices (separated by |):")
        self.label_prices.pack()
        self.entry_prices = tk.Entry(master)
        self.entry_prices.pack()

        self.label_quantities = tk.Label(master, text="Quantities (separated by |):")
        self.label_quantities.pack()
        self.entry_quantities = tk.Entry(master)
        self.entry_quantities.pack()

        # Create print button
        self.print_button = tk.Button(master, text="Create Receipt", command=self.print_receipt)
        self.print_button.pack()

    def print_receipt(self):
        customer = self.entry_customer.get()
        items = self.entry_items.get().split("|")
        prices = self.entry_prices.get().split("|")
        quantities = self.entry_quantities.get().split("|")

        prices = [float(price.strip()) for price in prices]
        quantities = [int(quantity.strip()) for quantity in quantities]

        # Create the receipt object
        receipt = GUIReceipt(customer, items, prices, quantities, self.master)

        # Print the receipt
        receipt.print_receipt()

        # Reset input fields
        self.entry_customer.delete(0, tk.END)
        self.entry_items.delete(0, tk.END)
        self.entry_prices.delete(0, tk.END)
        self.entry_quantities.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Create an instance of the app
app = ReceiptPrintingApp(root)

# Run the application
root.mainloop()
