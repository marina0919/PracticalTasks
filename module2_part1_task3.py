# Задание 3
# Пользователь вводит с клавиатуры два числа. Необ-
# ходимо найти максимум из двух чисел и показать его на
# экран.

number1 = int(input("Введите число1\n"))
number2 = int(input("Введите число2\n"))

if number1 >= number2:
    print("максимум из двух чисел", number1)
else:
    print("максимум из двух чисел", number2)
