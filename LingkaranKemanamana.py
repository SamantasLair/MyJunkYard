from manim import *

class Plane(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        
class MyAnimation(Scene):
    def construct(self):
        circle = Circle()

        self.play(Create(circle))

        # Move the circle around the screen
        for x in range(-4, 5):
            self.play(ApplyMethod(circle.move_to, np.array([x, x, 0])))
            self.play(ApplyMethod(circle.move_to, np.array([x-2, x, 0])))
            self.play(ApplyMethod(circle.move_to, np.array([x+1, x, 0])))

Plane().render()
MyAnimation().render()
