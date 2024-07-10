class Dog:
    # Class variable
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."


# Creating instances of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

# Accessing class variable
print(Dog.species)  # Output: Canis familiaris
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# Accessing instance variables
print(dog1.describe())  # Output: Buddy is 5 years old.
print(dog2.describe())  # Output: Milo is 3 years old.

# Modifying instance variables
dog1.age = 6
print(dog1.describe())  # Output: Buddy is 6 years old.

# Modifying class variable
Dog.species = "Canis lupus"
print(Dog.species)  # Output: Canis lupus
print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis lupus

# Changing class variable through instance
dog1.species = "New Species"
print(dog1.species)  # Output: New Species (changes only for this instance)
print(dog2.species)  # Output: Canis lupus (unchanged for other instances)
print(Dog.species)  # Output: Canis lupus (unchanged for the class itself)
