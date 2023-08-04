#used to store many items in a single variable,ordered,changeable,allow duplicates
#its one of the python collections(Arrays)
Afternoon = ["cathy","simon","jelly","cy"]

print(Afternoon)
#duplicating
Afternoon = ["cathy","simon","jelly","cy","cathy","cy"]
print(Afternoon)
#lists length
print(len(Afternoon))
#type
print(type(Afternoon))
#Accessing list items
print(Afternoon[4])
#negative indexing-no neg 0,start from last item
print(Afternoon[-4])
"""
  modifying lists
  newlist.append(4)
  newlist[2]=10
  newlist.remove[3]
"""
#accesing a range of items,includes 3 but excludes 5
print(Afternoon[3:5])

#prints items before index 4 not including 4
print(Afternoon[:4])
#leaving out the end inddex it calls for printing to the end of list
print(Afternoon[2:])
#changing specific item
Afternoon[2] = "jemily"
#add list items
Afternoon.append("Jemily")
print(Afternoon)
#insert allows you add an item at a specific position
Afternoon.insert(1,"Ximon")
print(Afternoon)
Afternoon.remove("simon")
print(Afternoon)
#removes the specific index or last item if index not specified
Afternoon.pop(1)
print(Afternoon)
#also removes the specified index
del Courses[0]
#for loops in lists
Courses = ["Bsse","Csc","Bist"]
for y in Courses:
    print(y) #prints each item one by one
 # checking if a certain item exists in the list
if "Csc" in Courses:
    print("Csc" +"is a course example")
    #determines how many items are in the list
    print (len(Afternoon))
    #making a copy of a list either by using the in built copy() or list() methods
    Afternoon = Courses.copy()
    print(Afternoon)
    #or
    Afternoon = list(Courses)
    print(Afternoon)
    #or
    Afternoon = Courses
    print(Afternoon)
Courses = ["Bsse","Csc","Bist"]
    #joining lists
new_list = Afternoon + Courses
print(new_list)
    #adding elements from one list to another with extend key word
Afternoon.extend(Courses)
print(Afternoon)
    #using the list()constructor to create a new list nb double parenthesis
Courses = list(("BSSE","CSC","BIST","BRAM"))
print(Courses)
    #clears the list or say empties the list
    #  Afternoon.clear()
  