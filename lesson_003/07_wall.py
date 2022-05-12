# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x = 1
y = 5
x1 = 10
y1 = 5
r=1
while r < 100:
    r+=1
    x+=10
    y+=5
    x1+=10
    y1+=5
    right_top = sd.get_point(x,y)
    left_bottom = sd.get_point(x1,y1)
    sd.rectangle(right_top=right_top, left_bottom=left_bottom, color=sd.COLOR_PURPLE, width=5)


sd.pause()