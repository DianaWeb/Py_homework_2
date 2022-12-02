""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

0,56 -> 11 """
num = float(input('Введите вещественное число: '))

my_sum = 0

while ((num).is_integer() == False):
    num = num * 10
else:
    while num > 0:
        my_sum = my_sum + num % 10
        num = num // 10
print(my_sum)
