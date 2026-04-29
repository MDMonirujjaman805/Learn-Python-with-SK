# Set Methods (add,remove,clear,pop,union,intersection)
collection = set()

print(collection)
collection.add(1)  # adds an element
collection.add(1)
collection.add((1, 2, 5, 6, 6, 6, 7, 5))
collection.add(4.56)
collection.add(True)
collection.add(False)
collection.add(False)
collection.add(True)
collection.add("monir")
collection.add("monir")
collection.add("world")
print(collection)
print(len(collection))

collection.remove(1)  # removes the an element
collection.remove(False)
print(collection)
print(len(collection))

# collection.clear() # empties the set
# print(collection)

collection.pop()  # removes a random value
print(collection)
print(len(collection))


collection2 = {3, 4, 5, 6, "monir", "md", "Monirujjaman", 7, 8, 8, 7, 6}
collection3 = {"monir", "md", 7, 8, 8, 7, 6, "Monirujjaman", "python", "js"}
print(collection2)
print(len(collection2))
print(collection3)
print(len(collection3))

collection4 = collection2.union(
    collection3
)  # combines both set values and returns new set
print(collection4)
print(len(collection4))


collection5 = {3, 4, 5, 6, "Monir", "MD", "Monirujjaman", 7, 8, 8, 7, 6}
collection6 = {"Monir", "MD", 7, 8, 8, 7, 6, "Monirujjaman", "python", "js"}
print(collection5)
print(len(collection5))
print(collection6)
print(len(collection6))

collection7 = collection5.intersection(
    collection6
)  # combines common values and returns new set
print(collection7)
print(len(collection7))
