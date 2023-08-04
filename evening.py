# EXERCISE

# Creating a dictionary
my_dict = {'car': 50000, 'bike': 2000, 'scooter': 1000}

# Using values() method to create a list of items from a dictionary
item_list = list(my_dict.values())
print(item_list)

# Checking if a specific key exists in a dictionary
if 'car' in my_dict:
    print("The key 'car' exists in the dictionary.")

# Changing and updating items in a dictionary
my_dict['bike'] = 2500
my_dict['motorcycle'] = 10000
print(my_dict)

# Adding and removing items from a dictionary
my_dict['truck'] = 60000
del my_dict['scooter']
print(my_dict)

# Looping through a dictionary and nesting dictionaries within dictionaries
nested_dict = {'person1': {'name': 'John', 'age': 35},
               'person2': {'name': 'Emily', 'age': 28}}

for key, value in nested_dict.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(f'{sub_key}: {sub_value}')

# Determining the length of a string using the len() function
my_string = "python is fun"
length = len(my_string)
print(length)

# Iterating through each character in a string using a for loop
for char in my_string:
    print(char)

# Slicing a string to extract specific portions of it
slice = my_string[7:13]
print(slice)

# Performing arithmetic operations with numbers and printing the results
a = 10
b = 4
sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b

print(f"Sum: {sum_result}")
print(f"Difference: {sub_result}")
print(f"Product: {mul_result}")
print(f"Division: {div_result}")

# Using boolean values and conditions to control program flow
condition = False

if condition:
    print("Condition is True")
else:
    print("Condition is False")


# CLASS PRACTICE
"""thisdict = {
  "brand": "iphone",
  "model": "13pro",
  "year": 2021
}
print(thisdict)
# using the get()
x = thisdict.get("model")
# change values
thisdict["year"] = 2023
# length of dict
print(len(thisdict))
# Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict)

x = 1    
y = 2.8  
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)
# FLOAT
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)
# COMPLEX
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1 
y = 2.8  
z = 1j 

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# CASTING
x = str("s1") 
y = str(2)    
z = str(3.0) 
 #STRINGS
 a = "Hello, World!"
print(len(a))

a = " Hello, World! "
print(a.strip())
print(a.lower())
print(a.upper())
print(a.split(","))
txt = "This is new"
x = "ew" in txt
print(x)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# booleans
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""