# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# Пример 5 -> 1 0 1 1 0
# 2

n = int(input('Введите 5 монеток через пробел: ')) # 1 0 1 1 0
coin = list(map(int, input(n:6). split())) 

var1 = 0 # орел
var2 = 0 # решка
for i in range(coin): ## как написать правильный цикл?
 if (coin [i] == 1):
    var1 += 1
    i += 1
else: var2 += 1
i += 1

if (var1 < var2):
   print(var1)
else:
   print(var2)

"""
n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
"""