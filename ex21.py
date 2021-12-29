def add(a, b):
    print(f"ADDING {a} and {b}:")
    return a + b


def substract(a, b):
    print(f"SUBTRACTING {a} and {b}:")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} and {b}:")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} and {b}:")
    return a / b


print("Let's do math with just functions.")

age = add(2, 8)
height = substract(90, 3)
weight = multiply(20, 10)
iq = divide(270, 9)

print(f"Age: {age}, height: {height}, weight: {weight}, and IQ: {iq}.")

# EXTRA

print("Here is a puzzle.")
what = add(age, substract(weight, height))
print("That becomes", what)


def sq(a):
    print(f"CALCULATE SQUARE of {a}")
    return a ^ 2


answer = sq(4)

print(f"What is {answer}")

print('-------------------------------')


def cal(a, b):
    return a * b


x = cal(3, 8)

print(x)

print('--------------------------------')


def cal2(a, b):
    print(f"calculating {a} * {b}")
    return a * b


print("ENTER the value of a")
a = int(input('>'))

print('ENTER the value of b')
b = int(input('>'))

y = cal2(a, b)

print(y)

# if you want to enter precise number, use float() with input.
