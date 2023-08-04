# EXCEPTION HANDLING
"""
Different types of exceptions in python:
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object,
such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.

"""
# Try and Except Statement
# Python program to handle simple runtime error

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")


# example 2
# Program to handle multiple errors with one
# except statement
def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


# Try with Else Clause
# Program to depict else clause with try-except
def mine(a, b):
    try:
        c = (a / b)
    except ZeroDivisionError:
        print("syntax error")
    else:
        print(c)


mine(2, 0)
mine(3, 3)

# Finally Keyword in Python
try:
    k = 5 // 0
    print(k)

# handles zero division exception
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    # this block is always executed regardless of exception generation.
    print('This is always executed')
# more examples
# In Python, you can define your own custom exceptions by creating
# a new class that inherits from the built-in Exception class or any of its subclasses.
# Here's an example of how you can define and use a custom exception:

class CustomException(Exception):
    pass

def divide(x, y):
    if y == 0:
        raise CustomException("Error: Division by zero!")
    return x / y

try:
    result = divide(10, 0)
    print("The result is:", result)

except CustomException as e:
    print(str(e))

finally:
    print("The program has finished.")

# Here are a few more examples of user-defined exceptions in Python:
# Example 1: Custom FileNotFoundError

class FileNotFoundError(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f"File not found: {self.file_name}"


def file_exists(file_name):
    pass


try:
    file_name = "nonexistent_file.txt"
    if not file_exists(file_name):
        raise FileNotFoundError(file_name)

except FileNotFoundError as e:
    print(str(e))

# Example 2: Custom InvalidInputError
class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value

    def __str__(self):
        return f"Invalid input: {self.input_value}"
def is_valid():
    pass
def process_input(input_value):
    if not is_valid():
        raise InvalidInputError(input_value)


try:
    input_value = "abc"
    process_input(input_value)

except InvalidInputError as e:
    print(str(e))


# FILE HANDLING
"""
-File handling in Python refers to the process of working with files, including reading from and writing to them.
 It enables programmers to manipulate files stored on a computer's file system, allowing them to store and retrieve data as needed.
  Python provides built-in functions and modules that make file handling straightforward and efficient.
Opening a file: To work with a file, you need to open it first. The open() function is used to open a file and returns a file object. 
File modes:
-'r': Read mode (default). The file is opened for reading.
-'w': Write mode. The file is opened for writing, and if it doesn't exist, a new file is created. If it exists, its contents are truncated.
-'a': Append mode. The file is opened for writing, and if it doesn't exist, a new file is created. If it exists, new data is appended to the end.
-'x': Exclusive creation mode. The file is opened for writing, but only if it doesn't already exist.
-'b': Binary mode. Used in combination with other modes, it opens the file in binary mode.
-'t': Text mode (default). Used in combination with other modes, it opens the file in text mode.
-Reading from a file: Once a file is open in read mode, you can read its contents using methods like read(), readline(), or readlines(). read() reads the entire file, readline() reads a single line, and readlines() reads all lines and returns them as a list.
-Writing to a file: When a file is open in write mode, you can write data to it using the write() method. You can write strings or use a loop to iterate over a collection of data and write each item to the file.
-Appending to a file: If a file is open in append mode, you can use the write() method to append data to the end of the file.
-Closing a file: After you finish working with a file, it's essential to close it using the close() method. Closing a file ensures that all data is written, and system resources are freed.
-Context managers: Python provides a convenient way to work with files using context managers. You can use the with statement to open a file, and it automatically takes care of closing the file when you're done, even if an exception occurs.
-File handling operations: Python's os module provides functions for file-related operations such as renaming files, deleting files, checking file existence, getting file information, and more
"""
#read a file
# Open the file in read mode
file = open('simon.txt', 'r')
# Read from the file
text = file.read()
print(text)

# Close the file
file.close()

#write to a file
# Open the file in write mode
file = open('simon.txt', 'w')
# Write content to the file
file.write('Hello,\n')
file.write('This is my file.')
# Close the file
file.close()

# appending to a file
# Open the file in append mode
file = open('simon.txt', 'a')
# Append content to the file
file.write('\nI love python.')
# Close the file
file.close()

# using context managers
# Open the file using a context manager
with open('simon.txt', 'r') as file:
    # Read the file content
    txt = file.read()
    print(txt)
# The file is automatically closed outside the 'with' block

# Handling exceptions in files
try:
    # Open the file in read mode
    with open('nonexistent.txt', 'r') as file:
        # Read the content
        txt = file.read()
        # Print the content
        print(txt)
except FileNotFoundError:
    print("File not found. Please ensure the file exists in the correct directory.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")



# using the os module
import os

# Rename a file
# os.rename('old.txt', 'new.txt')
# Delete a file
# os.remove('delete.txt')
# Check if a file exists
if os.path.exists('check.txt'):
    print("File exists!")
else:
    print("File does not exist.")
# Get file information
file_info = os.stat('simon.txt')
print(f"File size: {file_info.st_size} bytes")
print(f"Last modified: {file_info.st_mtime}")


# using the with statement
# Specify the file path
file_path = 'simon.txt'
try:
    # Open the file in write mode using a context manager
    with open(file_path, 'w') as file:
        # Write content to the file
        file.write('this is the new content\n')
        file.write('even this.')
    print(f"Data written to file '{file_path}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

