# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# здесь ваш код


start_point = sd.get_point(50, 50)
end_point = sd.get_point(350, 450)
sd.line(start_point=sd.get_point(50, 50),end_point=sd.get_point(355, 455),color=sd.COLOR_RED,width=4)
sd.line(start_point=sd.get_point(55, 55),end_point=sd.get_point(360, 460),color=sd.COLOR_ORANGE,width=4)
sd.line(start_point=sd.get_point(60, 60),end_point=sd.get_point(365, 465),color=sd.COLOR_YELLOW,width=4)
sd.line(start_point=sd.get_point(65, 65),end_point=sd.get_point(370, 470),color=sd.COLOR_GREEN,width=4)
sd.line(start_point=sd.get_point(70, 70),end_point=sd.get_point(375, 475),color=sd.COLOR_CYAN,width=4)
sd.line(start_point=sd.get_point(75, 75),end_point=sd.get_point(380, 480),color=sd.COLOR_BLUE,width=4)
sd.line(start_point=sd.get_point(80, 80),end_point=sd.get_point(385, 485),color=sd.COLOR_PURPLE,width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
#  здесь ваш код

sd.pause()
