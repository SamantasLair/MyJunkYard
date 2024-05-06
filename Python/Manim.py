
from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle().shift(DOWN*2)
        square = Square().to_corner(UL)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait(5)
