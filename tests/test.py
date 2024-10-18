from manim import *

class Test(Scene):
 def construct(self):
    texto = Tex("$\pi$")
    dot = always_redraw(lambda: 
                        Dot().next_to(texto, UP, buff=.5))
    c = Circle().scale(.7)
    self.add(texto, dot)
    self.play(texto.animate.shift(LEFT*3), run_time=1)
    self.play(ReplacementTransform(texto, c))
    dot_0 = Dot().move_to(dot.get_center())
    self.add(dot_0)
    for i in range(10):
        self.play(Rotate(dot_0, angle=PI*2, about_point=c.get_center(), rate_func=linear), run_time=1.5)

class Test1(Scene):
    def construct(self):
        vlt_num = ValueTracker(-4)
        gm_dot_0 = Dot(color=RED).set_x(vlt_num.get_value())
        gm_ln_0 = Line(start=[-4, 0, 0], end=[4, 0, 0], color=PURPLE_E,stroke_width=7)
        gm_dot_0.add_updater(lambda x: x.set_x(vlt_num.get_value()))
        tx_vlt_value = always_redraw(lambda: DecimalNumber(vlt_num.get_value(), num_decimal_places=2, font_size=22).next_to(gm_dot_0, DOWN, buff=.3))

        self.play(Write(gm_ln_0),Create(gm_dot_0), Write(tx_vlt_value)) 


        for _ in range(2):
            self.play(vlt_num.animate.set_value(4), run_time=4)
            self.play(vlt_num.animate.set_value(-4), run_time=4)

        



class TangentAnimation(Scene):
    def construct(self):
        ax = Axes()
        sine = ax.plot(np.sin, color=RED)
        alpha = ValueTracker(0)
        point = always_redraw(
            lambda: Dot(
                sine.point_from_proportion(alpha.get_value()),
                color=BLUE
            )
        )
        tangent = always_redraw(
            lambda: TangentLine(
                sine,
                alpha=alpha.get_value(),
                color=YELLOW,
                length=4
            )
        )
        self.add(ax, sine, point, tangent)
        for i in range(2):
            self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)
            self.play(alpha.animate.set_value(0), rate_func=linear, run_time=2)