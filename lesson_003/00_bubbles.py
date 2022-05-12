# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
#


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
#
def bubble(point, step) :
    radius = 50
    color = sd.random_color()
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color = color)
        radius += step

point = sd.get_point(500,500)



# Нарисовать 10 пузырьков в ряд
#  здесь ваш код




# Нарисовать три ряда по 10 пузырьков
#  здесь ваш код
for y in range (100,400,100):
    for x in range (100,1100,100):
        point = sd.get_point(x, y)
        bubble(point,5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# здесь ваш код
for _ in range (101):
    bubble(point=sd.random_point(), step = 5)


sd.pause()


