""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """
num = int(input('Введите число n: '))

product_num = 1

for i in range(1, num + 1):
    product_num = product_num * i
    print(product_num, end=' ')
