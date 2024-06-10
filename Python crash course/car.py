class Cat:
        #"""A simple attempt to model a dog."""

    def __init__(self, name, age):
        #"""initialize name and age attribute."""
        self.name = name
        self.age = age
    
    def sit(self):
        #"""simulate a dog sitting in respnse to a commond."""
        print(f"{self.name} in now sitting.")

    def roll_over(self):
        #"""simulate rolling over in response to a commond."""
        print(f"{self.name} rolled over!")

my_cat = Cat("mat", 6)
print(f"my cat's name is {my_cat.name}.")
print(f"my cat is {my_cat.age} years old.")
"""Calling Methods After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog"""