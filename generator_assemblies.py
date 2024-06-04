def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x * y

        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x / y

        return subtract


my_func_add = create_operation("add")
my_func_subtract = create_operation('subtract')
print(my_func_add(2, 3))
print(my_func_subtract(6, 3))
try:
    print(my_func_subtract(6, 0))
except ZeroDivisionError:
    print('Error: Division by zero')

multiply = lambda x: x * x
print(multiply(4))


def multiply_def(x):
    return x * x


print(multiply_def(4))


class Repeater:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, a, b):
        return a * b


f = Repeater(2, 4)
print(f(2, 4))
