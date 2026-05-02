def calc_sum(x, y, z):
    add = x + y + z
    return add


print(calc_sum(54, 66, 88))
print(calc_sum(55, 77, 89))
print(calc_sum(52, 45, 65))
print(calc_sum(54, 69, 84))


def hello():  # Without parameter,argument and return keyword.
    print("Hello")


hello()


def wel(name):
    a = "Hello! " + name
    return a


print(wel("Monir"))


def calc_prod(a=0, b=0):
    s = a + b
    return s


print(calc_prod())
