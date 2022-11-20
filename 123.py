from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculate_square_root(number):
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(number):
    if number <= 0:
        return

    print(f"Мы вычислили квадратный корень из введённого вами числа. 'Это будет: {calculate_square_root(number)}")


print(message)
calc(25.5)
