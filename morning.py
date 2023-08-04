
# EXERCISE1: Write a program to ask students about their mental health
student_mental_health = {}
student_name = input("Enter your name: ")
student_age = input("Enter your age: ")
mental_health_status = input("How would you rate your current mental health status on a scale of 1-10? ")
student_mental_health[student_name] = {"age": student_age, "mental health status": mental_health_status}

print("\nMental health information:")
for name, info in student_mental_health.items():
    print("Name:", name)
    print("Age:", info['age'])
    print("Mental Health Status:", info['mental health status'])


# if conditions
"""age = int(input())  # input is for user input
if age < 18:
    print("you are under age")
elif 18 <= age <= 65:  # elif age>=18 and age<=65:
    print("you are an adult")
else:
    print("you are a senior citizen")

# loops (for loop and while loop)
# for loop
cars = ["Tesla", "jeep", "ford", "toyota", "bmw"]
for i in cars:
    print(i)
fruits = ["mangoes", "oranges", "guavas", "passion"]
for fruit in fruits:
    print(fruit)

# while loop
# prints a condition as long as it's true
x = 0  # int(input())
while x < 5:
    print(x)
    x += 1
fruits = ["mangoes", "oranges", "guavas", "passion"]
fruits_count = 0
while fruits_count < len(fruits):
    print(fruits[fruits_count])
    fruits_count += 1

# break statement
for num in range(1,10):
    if num == 5:
        break
    print(num)

# continue statement
for m in range(1,10):
    if m == 5:
        continue
    print(m)

# exception handling(try, except and finally)
try:
    x=10/0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("this will always be executed")
emotions={
'happy':"am extremely happy",
'sad': "am sad , ican't even smile",
'angry': "I do hate anger because you act out of your mind",
}
user_emotion = input("how are you feeling today?")
if user_emotion  in emotions:
    print(emotions[user_emotion])
"""



