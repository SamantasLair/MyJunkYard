from manim import *

class Intro(Scene):
    def construct(self):
        intro = Text("Binary vs Sequential Search", font_size=36,t2c={"Binary":RED,"Sequential":BLUE})
        binary_search = Text("Binary Search", font_size=36,t2c={"Binary":RED}).shift(UP*0.75, RIGHT*0.75)
        sequential_search = Text("Sequential Search", font_size=36,t2c={"Sequential":BLUE}).shift(DOWN*0.75, LEFT*0.75)
        self.play(Write(intro))
        self.wait(3)
        self.play(Transform(intro, binary_search))
        self.wait(15)
        self.play(Transform(binary_search, sequential_search))
        self.wait(15)