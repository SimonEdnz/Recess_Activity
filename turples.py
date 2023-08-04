#ordered,inbuilt,unchangeable
phones = ("Techno","Iphone","Samsung")
print(phones)
#allow duplicate
phones = ("Techno","Iphone","Iphone","Sumsung")
print(phones)
#exercise-use len
print(len(phones))
#turple showing different data types
turple1 =("rice","Matooke")
turple2 = (100,200,300,400)
turple3 = ("sumsung",)#tuple with one item needs a trailing zero
print(type(turple2))
#accessing turples using indeces pos and neg
print(turple1[1])
print(turple2[-3])
#add item to turple
#first convert them to lists and after convert them back to turples
phones =  ("Techno","Iphone","Samsung")
z = list(phones)
z.append("Oppo")
phones = tuple(z)
print(phones)
#add tuples together
print(phones+turple2)
phones+=turple3
print(phones)
print(turple3)
#for loop in a tuple
for y in phones:
    print(y)