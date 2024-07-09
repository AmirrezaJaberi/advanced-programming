class ClassName:
    # Class attribute (optional)
    class_attribute = "some value"

    # Constructor to initialize instance attributes
    def __init__(self, param1, param2):
        self.instance_attribute1 = param1
        self.instance_attribute2 = param2

    # Instance method
    def method1(self):
        # Method implementation
        print(f"Instance Attribute 1: {self.instance_attribute1}")

    # Another instance method
    def method2(self, param):
        # Method implementation
        print(f"Instance Attribute 2: {self.instance_attribute2}, Param: {param}")

    # Special method for string representation
    def __str__(self):
        return f"ClassName(instance_attribute1={self.instance_attribute1}, instance_attribute2={self.instance_attribute2})"

    # Special method for object deletion (optional)
    def __del__(self):
        print(
            f"ClassName object with instance_attribute1={self.instance_attribute1} is being deleted"
        )

    # Property for a read-only attribute
    @property
    def read_only_property(self):
        return self.instance_attribute1

    # Property with a setter for a read-write attribute
    @property
    def read_write_property(self):
        return self.instance_attribute2

    @read_write_property.setter
    def read_write_property(self, value):
        self.instance_attribute2 = value
