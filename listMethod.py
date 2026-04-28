# List Methods (append,short(ascending & descending),reverse,insert,remove,extend)
marks = [45, 75, 34, 56, 87, 98, 65, 59, 32]
print(marks)
print(len(marks))
marks.append(99)
print(marks)
marks.sort()  # Ascending order
print(marks)
marks.sort(reverse=True)  # Descending order
print(marks)
marks.insert(3, 15)  # append new element(index,element)
print(marks)
marks.reverse()
print(marks)
marks.remove(98)  # remove first element form list based on element.
print(marks)
marks.pop(2)  # remove the element form list based on index.
print(marks)
print(len(marks))

marks1 = [45, 75, 34, 56, 87, 98, 65, 59, 32]
marks2 = [47, 77, 36, 58, 89, 100, 67, 61, 34]

marks1.extend(marks2)
print(marks1)
print(len(marks1))

text1 = [1, "abc", "abc", 1]
text2 = text1.copy()
print("1st original: ",text1)
print("2nd copy: ",text2)
print(type(text1))
print(type(text2))
