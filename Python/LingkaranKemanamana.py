from manim import *


class MyAnimation(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        self.wait(1)
        circle = Circle()
        square = Square()
        self.play(Create(circle))

        # Move the circle around the screen
        for x in range(-4, 5):
            self.play(ApplyMethod(circle.move_to, np.array([x, x, 10-x])))
            self.play(ApplyMethod(circle.move_to, np.array([x-2, x, 10-x])))
            self.play(ApplyMethod(circle.move_to, np.array([x+1, x, 10-x])))
        self.play(Transform(circle,square))
MyAnimation().render()
