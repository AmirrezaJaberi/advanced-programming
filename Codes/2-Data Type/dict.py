# Create a dictionary with student details using the dict() function
student_dict = dict(name="Amirreza Jaberi", student_id="123456", gpa=3.5)

# Print the original dictionary
print("Original dictionary:", student_dict)
# Output: {'name': 'Amirreza Jaberi', 'student_id': '123456', 'gpa': 3.5}

# Add an element to the dictionary
student_dict["major"] = "Computer Engineering"
print("After adding 'major':", student_dict)
# Output: {'name': 'Amirreza Jaberi', 'student_id': '123456', 'gpa': 3.5, 'major': 'Computer Engineering'}

# Remove an element from the dictionary
del student_dict["gpa"]
print("After removing 'gpa':", student_dict)
# Output: {'name': 'Amirreza Jaberi', 'student_id': '123456', 'major': 'Computer Engineering'}

# Replace an element in the dictionary
student_dict["name"] = "Alireza Jaberi"
print("After replacing 'name':", student_dict)
# Output: {'name': 'Alireza Jaberi', 'student_id': '123456', 'major': 'Computer Engineering'}
