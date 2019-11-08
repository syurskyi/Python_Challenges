# Двоичные числа

# Шестнадцатеричные числа

# Восьмеричные числа


# Вещественное число
# # # 3.2 * 10**5

# # # 1 * 10**(-3)

# # # 10000.0

# Компексные числа

# int

# float

# bin

# oct

# hex

# round

# round second parameter

# аbs

# pow

# divmod(x, y)

# degrees ()

# radians ()

# ceil ()

# floor ()

# fmod()

#  построение вещественного значения
# # из строки

# Cоздать Рациональные числа
# # # Числитель, знаменатель

# # # Будет упрощено до

# # # Рациональные числа могут создаваться из строк с представлением вещественных чисел

# numerator and denominator
from fractions import Fraction

x = Fraction(22, 7)

# Truncation

# Truncate create function
def truncate():
    pass

# Floor()

# create round_half_up function
# using floor
def round_half_up():
    pass

# ceil

# create round_half_down function
# using ceil
def round_half_down():
    pass

# Let’s write a function called round_up() that implements the “rounding up” strategy
def round_up():
    pass

# create  round_half_away_from_zero
# using copysign
def round_half_away_from_zero():
    pass

# Decimals have context and local...
# # # Global Context:

g_ctx = None

# We can change settings in the global context:


# # # The localcontext() function will return a context manager that we can use with a with statement:


# # # Modifying the local context has no effect on the global context


# # # Decimals - Rounding
from decimal import Decimal

x = Decimal('1.25')
y = Decimal('1.35')



x = Decimal('1.25')
y = Decimal('1.35')


# Decimals: Constructors and Contexts

# # # Integers

# # # Strings

# # # Tuples

# # # But don't use Floats

# random

# random seed

# random uniform

# randint

# randrange

# choice

# shuffle
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sample
# string example

# number example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Случайный элемент последовательности


# Подпоследовательность из трёх элементов последовательности


# Значение больше чем первый аргумент и не строго меньше чем второй


# Случайное число из промежутка от 0 до 10


# Случайное число из промежутка от 0 до 101 с шагом 7


# Стандартный random.Random
# работает на основе генератора псевдослучайных чисел Вихрь Мерсенна.
# Можно создавать свои подклассы, реализующие другие генераторы.

class MyRandom():
    pass

# int , float info