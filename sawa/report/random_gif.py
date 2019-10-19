from Young.Young_pattern import Young_Pattern
from sawa.test import gif_maker

YP = Young_Pattern(3, 6, 15, -5)
gif_maker(generation=10, duration=1000, YP=YP, img_path="random_YP_duration1000.gif")



