class Person:
    # Constructor to initialize the object's attributes
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Special method to convert object to string (for display)
    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"

    # Special method to determine the length (e.g., length of the name)
    def __len__(self):
        return len(self._name)

    # Special method to delete the object
    def __del__(self):
        print(f"Person {self._name} is being deleted")

    # Property for 'name' attribute
    @property
    def name(self):
        return self._name

    # Setter for 'name' attribute
    @name.setter
    def name(self, value):
        self._name = value

    # Property for 'age' attribute
    @property
    def age(self):
        return self._age

    # Setter for 'age' attribute
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")


# Reading input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Creating an instance of the Person class
person = Person(name, age)

# Using the __str__ method to display the object
print(person)  # Output: Person(name=YourName, age=YourAge)

# Using the __len__ method to display the length of the name
print(len(person))  # Output: Length of the name

# Using properties and setters
print(person.name)  # Output: YourName
person.name = "NewName"
print(person.name)  # Output: NewName

print(person.age)  # Output: YourAge
person.age = 25
print(person.age)  # Output: 25

# Deleting the object
del person
