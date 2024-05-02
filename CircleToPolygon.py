from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle()
        dot = np.array([1,2,0])
        dot2 = np.array([-1,2,0])
        dot3 = np.array([-2,0,0])
        dot4 = np.array([-1,-2,0])
        dot5 = np.array([1,-2,0])
        dot6 = np.array([2,0,0])
        polygon = Polygon(dot, dot2, dot3, dot4,dot5, dot6, fill_color=BLUE, fill_opacity=1)

        self.play(Create(polygon))
        self.play(Transform(polygon, circle))
        self.wait(2)

MyAnimation().construct()
