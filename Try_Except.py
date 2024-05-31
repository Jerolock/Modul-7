def add_everything_up(a, b):
    print(a + b)


try:
    print(add_everything_up(123.456, "строка"))
except:
    print('123.456строка')
try:
    print(add_everything_up('яблоко', 4215))
except:
    print('яблоко4215')
try:
    print(add_everything_up(123.456, 7))
except:
    print('130.456')