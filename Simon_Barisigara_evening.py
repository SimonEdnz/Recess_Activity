# Create a list with 5 items (names of people) and write a Python program to output the 2nd item.
people = ["simon", "Bin", "jim", "David", "Evans"]
print(people[1])

# Write a Python program to change the value of the first item to a new value
people[0] = "Douglas"
print(people)

# Write a Python program to add a sixth item to the list
people.append("Jamal")
print(people)

# Write a Python program to add "Bathel" as the 3rd item in your list
people.insert(2, "Bathel")
print(people)

# Write a Python program to remove the 4th item from the list
del people[3]
print(people)

# Use negative indexing to print the last item in your list.
print(people[-1])

# Create a new list with 7 items and use a range of indexes to print the 3rd, 4th, and 5th items
nums = [11, 22, 33, 44, 55, 66, 77]
print(nums[2:5])

# Write a list of countries and make a copy of it
countries = ["Uganda", "kenya", "tanzania", "rwanda"]
EastAfrica = countries.copy()
print(EastAfrica)

# Write a Python program to loop through the list of countries
for country in countries:
    print(country)

# Write a list of animal names and sort them in both descending and ascending order
animals = ["lion", "tiger", "elephant", "giraffe", "zebra"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

# Using the list above, write a Python program to output only animal names with the letter 'a' in them.
animals_a = [name for name in animals if 'a' in name.lower()]
print(animals_a)

# Write two lists, one containing your first names and the other your second names. Join the two lists
first_name = ("Simon")
second_name = ("Bin")
full_name = first_name + second_name
print(full_name)

# EXERCISE 2
# Write a python program to output your favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[3]
print(favorite_phone_brand)

# Use negative indexing to print the 2nd last item in your tuple
second_last_item = x[-2]
print(second_last_item)

# Using the phones list above, write a python program to update “iphone” to “itel”
updated_x = list(x)
updated_x[1] = "itel"
x = tuple(updated_x)
print(x)

# Write a python program to add “Huawei” to your tuple
x = x + ("Huawei",)
print(x)

# Write a python program to loop through the tuple above
for item in x:
    print(item)

# Write a python program to remove/delete the first item in your tuple
x = x[1:]
print(x)

# Using the tuple() constructor, create a tuple of the cities in Uganda
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])

#  Write a python program to unpack your tuple
print(cities)

# Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print(cities[1:3])

#  Create a tuple of colors and multiply it by 3
colors = ("red", "blue")
multiply_colors = colors * 3
print(multiply_colors)

# Return the number of times 8 appears in this tuple
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = this_tuple.count(8)
print(count)

# EXERCISE 3
# Use the set() constructor to create a set of 3 of your favorite beverages
beverages = set(["coffee", "tea", "milk"])
print(beverages)

# Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.update(["soda", "smoothie"])
print(beverages)

# Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

# Write a python program to remove “kettle” from the set above
mySet.remove("kettle")
print(mySet)

# Write a python program to loop through the set above.
for item in mySet:
    print(item)
# Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in
# the set
mySet = {11, 22, 33, 44}
myList = [55, 66]
mySet.update(myList)
print(mySet)

# EXERCISE4
# Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
x = 10
string = " cows"
result = str(x) + string
print(result)

# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
print(txt.strip())

#  Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())

#  Write a python program to replace character ‘U’ with ‘V’ in the string above.
new_txt = txt.replace('U', 'V')
print(new_txt)

# Using the code below, write a python program to return a range of characters in the 2nd,3rd and 4th position
y = "I am proudly Ugandan"
print(y[1:4])

# The piece of code below will give an error when output;  x = “All “Data Scientists” are cool!”
# Write a python program to correct it
x = 'All "Data Scientists" are cool!'
print(x)

# EXERCISE 5
# 5.1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

# Write a Python program to change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print(Shoes)

# Write a Python program to add a key/value pair "type": "sneakers" to the dictionary.
Shoes["type"] = "sneakers"
print(Shoes)

# Write a Python program to return a list of all the keys in the dictionary above
keys = list(Shoes.keys())
print(keys)

# Write a Python program to return a list of all the values in the dictionary above
values = list(Shoes.values())
print(values)

# Check if the key "size" exists in the dictionary above
if "size" in Shoes:
    print("Key 'size' exists")
else:
    print("Key 'size' does not exist")

# Write a Python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, ":", value)

# Write a Python program to remove "color" from the dictionary
del Shoes["color"]
print(Shoes)

# Write a Python program to empty the dictionary above
Shoes.clear()
print(Shoes)

# Write a dictionary of your choice and make a copy of it.
original_dict = {"a": 1, "b": 2, "c": 3}
copy_dict = original_dict.copy()
print(copy_dict)

# Creating a nested dictionary
student_records = {
    "John": {
        "age": 21,
        "major": "Computer Science",
        "grades": {
            "math": 95,
            "english": 87,
            "history": 92
        }
    },
    "Emily": {
        "age": 20,
        "major": "Biology",
        "grades": {
            "math": 78,
            "english": 84,
            "biology": 91
        }
    }
}

# Accessing nested dictionary values
print("John's age:", student_records["John"]["age"])
print("Emily's major:", student_records["Emily"]["major"])
print("John's math grade:", student_records["John"]["grades"]["math"])
print("Emily's biology grade:", student_records["Emily"]["grades"]["biology"])
