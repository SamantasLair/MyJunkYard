
from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(circle))

# To run the animation, add the following line:
MyAnimation().construct()