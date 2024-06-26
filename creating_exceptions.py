class InvalidDataException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


class ProcessingException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info


def f(person_name):
    if type(person_name) == int:
        raise InvalidDataException('числа вводить нельзя >:(', person_name)


try:
    f(123)
except InvalidDataException as e:
    print('Ай-я-я-яй, как не хорошо')
    print(f'Сообщение об ошибке: {e.message}')
    print(f'И вот почему: {e.info}')


class Car:
    def __init__(self, maximum_speed, speed):
        self.maximum_speed = maximum_speed
        self.speed = speed


def trip(speed, maximum_speed):
    if speed == maximum_speed:
        raise ProcessingException('Сейчас будет перегрев двигателя, тормозите', speed)


try:
    print(trip(120, 120))
except ProcessingException as eq:
    print('Ай-я-я-яй, как не хорошо')
    print(f'Сообщение об ошибке: {eq.message}')
    print(f'И вот почему: {eq.info}')
