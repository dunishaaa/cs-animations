from manim import *


class Cuadrantes(Scene):
    def construct(self):
        # ss
        tx_ejem_1 = Text(
            "Un ejercicio con cuadrantes...", t2c={"ejercicio": BLUE}, font_size=44
        )
        self.play(Write(tx_ejem_1))
        self.wait(1)
        self.play(Unwrite(tx_ejem_1), run_time=0.7)
        axes = NumberPlane().set_opacity(0.4).add_coordinates()
        self.play(Write(axes, run_time=6))

        arr_rom_cuad = ["I", "II", "III", "IV"]
        palette = [GREEN_E, RED_E, PURPLE_E, ORANGE]
        pos_tx = [UR, UL, DL, DR]
        arr_coord = ["(+, +)", "(-, +)", "(-, -)", "(+, -)"]
        cond_tx = [
            r"$x > 0$ \&\& $y > 0$",
            r"$x < 0$ \&\& $y > 0$",
            r"$x < 0$ \&\& $y < 0$",
            r"$x > 0$ \&\& $y < 0$",
        ]
        rect_pos = [
            [3.55, 2.05, 0.0],
            [-3.55, 2.05, 0.0],
            [-3.55, -2.05, 0.0],
            [3.55, -2.05, 0.0],
        ]
        quadrants = VGroup(
            *[
                Rectangle(height=4, width=7, color=BLUE_D)
                .set_opacity(0.3)
                .move_to(rect_pos[i])
                for i in range(4)
            ]
        )

        tx_cuad_rom = [
            Tex(f"\\textbf{{{arr_rom_cuad[i]}}}", font_size=40)
            .move_to(pos_tx[i] * [3.5, 2.0, 0])
            .set_color(palette[i])
            for i in range(4)
        ]
        tx_cuad_sign = [
            MathTex(f"\\textbf{{{arr_coord[i]}}}", font_size=30)
            .next_to(tx_cuad_rom[i], DOWN, buff=0.2)
            .set_color(palette[i])
            for i in range(4)
        ]
        tx_cond = [
            Tex(
                f"{arr_rom_cuad[i]}.- \\textbf{{{cond_tx[i]}}}",
                font_size=27,
                color=palette[i],
            ).next_to(tx_cuad_sign[i], DOWN, buff=0.2)
            for i in range(4)
        ]
        self.wait(4)

        for quad in quadrants.submobjects:
            self.play(GrowFromPoint(quad, quad.get_center()), run_time=0.7)
        # ss

        for i, quad in enumerate(quadrants.submobjects):
            self.play(
                quad.animate.set_color(palette[i]).set_opacity(0.5).scale(1.1),
                run_time=0.7,
            )
            self.play(
                quad.animate.set_opacity(0.2).scale(1 / 1.1),
                run_time=0.5,
            )
            self.play(Write(tx_cuad_rom[i]))
            self.play(Write(tx_cuad_sign[i]))
            self.play(
                Indicate(tx_cuad_sign[i], scale_factor=1.6, run_time=1),
                Wiggle(tx_cuad_sign[i], n_wiggles=20, run_time=1),
                Write(tx_cond[i], run_time=2.0),
            )
            self.wait(0.7)
        # ss

        past_scene = Group(*self.mobjects)
        texts = VGroup(*tx_cond)

        self.play(past_scene.animate.scale(0.5).to_edge(LEFT, buff=1))
        self.play(
            texts.animate.scale(2.5)
            .arrange(DOWN, buff=0.5)
            .next_to(past_scene, RIGHT, buff=0.7),
            *[
                quad.animate.set_opacity(0.5)
                for i, quad in enumerate(quadrants.submobjects)
            ],
        )
        self.wait(10)
        # rs

        self.play(FadeOut(texts), FadeOut(past_scene))

        tx_outro = Text("Muchas gracias por ver el video")
        tx_outro2 = Text("y recuerda seguir practicando...")

        self.play(Write(tx_outro))
        self.wait(8)
        self.play(Unwrite(tx_outro, reverse=False, run_time=0.8), Write(tx_outro2))
        self.wait(1.5)
        self.play(FadeOut(tx_outro2))
        self.wait(3)
