# Реализуйте алгоритм перемешивания списка.

import random
my_list = [-1, 2, -3, 4, 5]
for i in range(len(my_list)):
    n = random.randint(0, len(my_list) - 1)
    my_list[i], my_list[n] = my_list[n], my_list[i]
    print(my_list[i], my_list[n])
print(my_list)
