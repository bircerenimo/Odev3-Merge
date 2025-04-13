def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("5 + 3 =", add(5, 3))
print("10 / 2 =", divide(10, 2))
