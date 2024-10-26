from manim import *

class Cuadrantes(Scene):
    def construct(self):
        self.next_section()
        tx_ejem_1 = Text("Un ejemplo con cuadrantes...", font_size=44)
        self.play(Write(tx_ejem_1))
        self.play(Unwrite(tx_ejem_1))
        axes = NumberPlane().set_opacity(.4).add_coordinates()
        self.play(Write(axes))
        self.wait(.5)

        arr_rom_cuad = ["I", "II", "III", "IV"]
        palette = [GREEN_E, RED_E, PURPLE_E, ORANGE]
        pos_tx = [UR, UL, DL, DR]
        arr_coord = ["(+, +)", "(-, +)", "(-, -)", "(+, -)"]
        cond_tx = [
            "$x > 0$ \&\& $y > 0$",
            "$x < 0$ \&\& $y > 0$",
            "$x < 0$ \&\& $y < 0$",
            "$x > 0$ \&\& $y < 0$"
        ]
        rect_pos = [
           [3.55, 2.05, 0.],                                                                             
           [-3.55, 2.05, 0.],                                                                             
           [-3.55, -2.05, 0.],                                                                             
           [3.55, -2.05, 0.],                                                                             
        ]
        quadrants = VGroup(*[
            Rectangle(height=4, width=7, color=BLUE_D).set_opacity(.3).move_to(rect_pos[i])
            for i in range(4)
        ])

        

        tx_cuad_rom =   [
            Tex(f'\\textbf{{{arr_rom_cuad[i]}}}', font_size=40).move_to(pos_tx[i]*[3.5, 2.0,0]).set_color(palette[i]) for i in range(4)
        ]
        tx_cuad_sign =  [
            MathTex(f'\\textbf{{{arr_coord[i]}}}', font_size=30).next_to(tx_cuad_rom[i], DOWN, buff=.2).set_color(palette[i]) for i in range(4)
        ]
        tx_cond = [
            Tex(
                f'{arr_rom_cuad[i]}.- \\textbf{{{cond_tx[i]}}}',
                font_size=27,
                color=palette[i]
            ).next_to(tx_cuad_sign[i], DOWN, buff=.2) for i in range(4)
        ]

        self.next_section()
        for quad in quadrants.submobjects:
            self.play(GrowFromPoint(quad, quad.get_center()))
            

        for i,quad in enumerate(quadrants.submobjects):
            self.play(quad.animate.set_color(palette[i]).set_opacity(.5).scale(1.1), run_time=.7)
            self.play(quad.animate.set_color(BLUE_D).set_opacity(.3).scale(1/1.1), run_time=.7)
            self.play(Write(tx_cuad_rom[i]))
            self.play(Write(tx_cuad_sign[i]))
            self.play(
                Indicate(tx_cuad_sign[i], scale_factor=1.6, run_time=2), 
                Wiggle(tx_cuad_sign[i], n_wiggles=20, run_time=2),
                Write(tx_cond[i], run_time=1.5)
                )
        

        past_scene = Group(*self.mobjects)
        texts = VGroup(*tx_cond)
#        ifs = Tex(
#            r"\begin{enumerate}"
#            f"\\item {cond_tx[0]}"
#            f"\\item {cond_tx[1]}"
#            f"\\item {cond_tx[2]}"
#            f"\\item {cond_tx[3]}"
#            r"\end{enumerate}"
#            ).set_color(YELLOW)
#        self.play(ReplacementTransform(texts, ifs))

        self.next_section()
        self.play(past_scene.animate.scale(.5).to_edge(LEFT, buff=1))
        self.play(
            texts.animate.scale(2.5).arrange(DOWN, buff=.5).next_to(past_scene, RIGHT, buff=.7),
            *[quad.animate.set_color(palette[i]) for i, quad in enumerate(quadrants.submobjects)]
        )


        


        self.wait(2)
        
