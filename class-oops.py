# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute
#     def bark(self):
#         print(self.name)

# dog1 = Dog("Buddy", 3)
# dog1.bark()    
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# # Access class and instance variables
# print(dog1.species)  # (Class variable)
# print(dog1.name)     # (Instance variable)
# print(dog2.name)     # (Instance variable)

# # Modify instance variables
# dog1.name = "Max"
# print(dog1.name)     # (Updated instance variable)

# # Modify class variable
# Dog.species = "Feline"
# print(dog1.species)  # (Updated class variable)
# print(dog2.species)

# Parent Class
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method

# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()

# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type


# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments




def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)