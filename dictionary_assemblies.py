def squar(x):
    return x * x


def odd(x):
    return x % 2


dict1 = [1, 2, 5, 12, 11, 35, 4, 89, 10]

result = map(squar, filter(odd,dict1))
print(list(result))
