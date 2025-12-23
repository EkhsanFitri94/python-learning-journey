name = "Ekhsan" # This is a String
age = 31 # This is an Integer
price = 19.99 # This is a Float
is_student = True # This is a Boolean
courses = ["Business", "Administration", "AI"] # This is a List
person = {"name": "Ekhsan", "age": 31} # This is a Dictionary
fruits = ("apple", "banana", "cherry") # This is a Tuple
unique_numbers = {1,2,3,2} # This is a Set  
pi = 3.14159 # This is a Constant
def greet():
    return f"Hello, my name is {name} and I am {age} years old."
print(greet())
# This code snippet demonstrates various data types in Python including String, Integer, Float, Boolean, List, Dictionary, and Constant.
print("Data Types in Python:")
print(f"String: {name} (Type: {type(name)})")
print(f"Integer: {age} (Type: {type(age)})")
print(f"Float: {price} (Type: {type(price)})")
print(f"Boolean: {is_student} (Type: {type(is_student)})")
print(f"List: {courses} (Type: {type(courses)})")
print(f"Dictionary: {person} (Type: {type(person)})")
print(f"Constant: {pi} (Type: {type(pi)})")
# End of storing_data.py

print("Hello, World! My name is Muhammad Ekhsan Fitri Bin Zamrus, and I am a software developer in training.")

age = 31
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count = count + 1 # Don't forget to change the condition!

def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

greet("Ekhsan") # Call the function
greet("Teya") # Call it again with a different name

user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")