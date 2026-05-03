f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

g = open("demo.txt", "w")
g.write("I want to learn JavaScript tomorrow.")
g.close()

h = open("demo.txt", "a")
h.write(" 123")
h.close()
