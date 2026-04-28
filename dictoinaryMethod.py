# Dictionary Methods (keys,values,items,get,update)
student = {
    "name": "monir",
    "age": 43,
    "marks": 88.45,
    "subjects": ["Python", "JavaScript", "C++"],
    "results": (88.45, 85.45, 86.99),
    "isStudent": True,
}
print(student)
print(student.keys())  # return all keys.
print(type(student.keys()))
print(len(student))

# Type Casting: Convert dict type to list type with length.
a = list(student.keys())
print(len(a))
print(type(a))

# Type Casting: Convert dict type to tuple type
print(tuple(student.keys()))
print(type(tuple(student.keys())))

print(student.values())  # return all values.
print(type(student.values()))

print(student.items())  # return all keys-values pairs as (Tuple).
print(type(student.items()))

print(student["subjects"]) # if mistake Throw Error
print(student.get("subjects"))  # return the keys according to values. # if mistake Throw not Error
print(type(student.get("subjects")))

student.update({"full_name": "Monirujjaman"}) # inserts the key_value_pair,multiple key_value_pair and new_Dictionary.
print(student)

new_dict = student.update({"city": "Gazipur"})
print(student)
