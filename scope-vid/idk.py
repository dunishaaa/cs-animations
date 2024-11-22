from manim import *


class Prueba(Scene):
    def construct(self):
        gm = Rectangle()

        # ss
        dot = Dot(color=YELLOW).move_to(gm.get_center())
        # dot.add_updater(lambda s: s.move_to(gm.get_center()))
        trace = TracedPath(
            dot.get_center,
            stroke_color=[YELLOW, PURPLE],
            dissipating_time=0.5,
        )

        dot.add_updater(lambda s: s.move_to(gm.get_center()))
        self.add(trace)
        self.play(Create(gm), Create(dot))

        # rs
        for i in range(10):

            self.play(gm.animate.shift(RIGHT * 4))

            self.play(gm.animate.shift(LEFT * 4))


class Prueba2(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(100)]).arrange_in_grid(10, 10)

        self.play(Create(dots))

        for i in range(20):
            self.play(Write(dots))
            self.play(FadeOut(dots))

        self.wait(2)
