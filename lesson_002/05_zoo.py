#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]


# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
#  здесь ваш код
zoo.insert(1,'bear')
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
#  здесь ваш код
zoo.extend(birds)
print(zoo)
# уберите слона
#  и выведите список на консоль
#  здесь ваш код
del zoo[2]
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
#  здесь ваш код
lion_index = zoo.index("lion") + 1
lark_index = zoo.index('lark') + 1
print(lion_index, lark_index)

