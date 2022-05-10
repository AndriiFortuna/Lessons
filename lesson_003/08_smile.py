# -*- coding: utf-8 -*-

# (определение функций)

import simple_draw
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


radius = 50
center_position = simple_draw.get_point(100,100)
simple_draw.circle(radius=radius, color = simple_draw.COLOR_PURPLE, width=3,center_position=center_position )

radius1 = 10
center_position = simple_draw.get_point(130,110)
simple_draw.circle(radius=radius1, color = simple_draw.COLOR_YELLOW, width=7,center_position=center_position )

radius2 = 10
center_position = simple_draw.get_point(70,110)
simple_draw.circle(radius=radius1, color = simple_draw.COLOR_YELLOW, width=7,center_position=center_position )
simple_draw.lines(point_list=[simple_draw.get_point(85,85),simple_draw.get_point(100,70),simple_draw.get_point(110,85)],color = simple_draw.COLOR_PURPLE, width=3 )




simple_draw.pause()
