# Dictionary Basics
student = {
    "name": "monir",
    "age": 43,
    "marks": 88.45,
    "subjects": ["Python", "JavaScript", "C++"],
    "results": (88.45, 85.45, 86.99),
    "isStudent": True,
}
print(student)
print(type(student))

# Accessing Dictionary
print(student["name"])
print(student["subjects"])
print(student["results"])

# Mutable the value
student["name"] = "Monirujjaman"
print(student)

# New key value Assigning
student["sur_name"] = "MD"
student["full_name"] = student["sur_name"] + " " + student["name"]
print(student)

# Declare a null Dictionary
null_dictionary = {}
print(null_dictionary)

# Nested Dictionaries
institute = {
    "name": "Programming Hero",
    "address": "Dhaka",
    "course_details": {"Python": 8, "next level": 6, "web development": 9},
    "language": {"Python": "3 months", "JS": "5 months", "C": "9 months"},
    "phone": +880 - 1234567891,
}
print(institute)
print(type(institute))

print(institute["course_details"])
print(type(institute["course_details"]))

# Accessing value of Nested Dictionaries
print(institute["course_details"]["Python"])

abc = institute["course_details"]
xyz = institute["language"]

print(abc)
print(type(abc))

print(xyz)
print(type(xyz))
