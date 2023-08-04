
# create a simple calculator program  to calculate (add, subtract, multiply,divide) with GUI interface
# make the title of the calculator program window with your name e.g. Simon calculator

import tkinter as tk


def add():
    x = float(entry_x.get())
    num2 = float(entry_y.get())
    result = x + num2
    my_result.config(text="Result: " + str(result))


def subtract():
    x = float(entry_x.get())
    y = float(entry_y.get())
    result = x - y
    my_result.config(text="Result: " + str(result))


def multiply():
    x = float(entry_x.get())
    num2 = float(entry_y.get())
    result = x * num2
    my_result.config(text="Result: " + str(result))


def divide():
    x = float(entry_x.get())
    y = float(entry_y.get())
    if y != 0:
        result = x / y
        my_result.config(text="Result: " + str(result))
    else:
        my_result.config(text="Error:syntax error")


# Create the main window
window = tk.Tk()
window.title("Barisigara Simon Simple Calculator")

# Create entry fields for numbers
nte_x = tk.Label(window, text="First num:")
nte_x.pack()
entry_x = tk.Entry(window)
entry_x.pack()

ente_y = tk.Label(window, text="Second num:")
ente_y.pack()
entry_y = tk.Entry(window)
entry_y.pack()

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Create buttons
button_add = tk.Button(button_frame, text="+", command=add)
button_add.pack(side=tk.LEFT, padx=5)

button_subtract = tk.Button(button_frame, text="-", command=subtract)
button_subtract.pack(side=tk.LEFT, padx=5)

button_multiply = tk.Button(button_frame, text="*", command=multiply)
button_multiply.pack(side=tk.LEFT, padx=5)

button_divide = tk.Button(button_frame, text="/", command=divide)
button_divide.pack(side=tk.LEFT, padx=5)

# displaying result
my_result = tk.Label(window, text="ANS:")
my_result.pack()

# Start the main loop
window.mainloop()

# class work
"""a = 15
b = 9
# greater than
if a > b:
    print("a is greater than b")
    print(a > b)
# less than
if a < b:
    print("a is less than b")
    print(a < b)
# greater or equal to
if a >= b:
    print("a is greater or equal to b")
    print(a >= b)
# less than or equal
if a <= b:
    print("a is less than or equal to b")
    print(a <= b)
# equal to
if a == b:
    print("a is  equal to b")
    print(a == b)
# not equal
if a != b:
    print("a is not equal to b")
    print(a != b)
# less than or equal to
print(a <= b)

# logical operators
a = True
b = False
# logical AND
if a and b:
    print(a and b)
    # logical OR
    print(a or b)
    # logical NOT
    print(not a)
    print(not b)
# assignment operator
# compound operators
a = 5
# add and assign
a += 5
print(a)
# subtract and assign
b = 18
b -= 9
print(b)
# exponential and assign
f = 2
f **= 3
print(f)
# membership assignment operators
cars = ["bmw", "jeep", "tesla", "toyota"]
if 'jeep' in cars:
    print("it exists in list")
    print('raum' in cars)
# identity operators
x = 10
y = 10
print(x is y)
print(x is not y)
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
# bitwise operators are used to perform bits in form of binary number
# bitwise AND(&)
# bitwise OR(|)
# bitwise XOR(^)
# bitwise NOT(~) flips numbers
# bitwise LEFT SHIFT(<<)
# bitwise RIGHT SHIFT(>>)
a = 10
b = 20

print(a & b)
print(a | b)
print(a ^ b)
print(~ b)
print(~ a)
print(a << b)
print(a >> b)
"""

