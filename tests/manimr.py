from manim import *


class P(Scene):
    def construct(self):
        c = Circle(color="BLUE")
        self.play(Write(c))
