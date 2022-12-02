""" Задайте список из N элементов, заполненных числами из промежутка[-N, N].
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
- -> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0
 """
n = int(input('Введите число для списка: '))
my_list = list(range(-n, n + 1))
print(my_list)

indexes = (input('Введите индексы:  '))
# print(indexes)
# print(type(indexes))
my_str = indexes.split(' ')
# print(my_str)
nums = list(map(int, my_str))
# print(nums)

result = 1
for i in range(len(nums)):
    j = int(nums[i])
    print(my_list[j], end=' ')
    result = result * my_list[j]
print(result)
