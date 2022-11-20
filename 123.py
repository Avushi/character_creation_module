from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(number):
    """Принимает значение для расчета."""
    result = calculate_square_root(number)
    if number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {result}')


print(message)
calc(25.5)
