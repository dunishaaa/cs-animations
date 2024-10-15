from manim import *


class Intro(Scene):
    def construct(self):
        tx_que_funcion = Tex("¿Qué es una función?").scale(1.4)
        self.play(Write(tx_que_funcion))

        tx_que_funcion.generate_target()
        tx_que_funcion.target.to_edge(UP)
        tx_expl_funcion = Tex(
            "Una función es un bloque de código que realiza alguna operación" 
            ).scale(.8).next_to(tx_que_funcion.target, DOWN, buff=1)
        self.play(MoveToTarget(tx_que_funcion))
        self.play(Write(tx_expl_funcion))

        #podemos tener la funcion trianguloPorCuadrado

        gm_arr_0 = Arrow().scale(2)
        gm_tr_0 = Triangle().scale(1.2).next_to(gm_arr_0, LEFT, buff=.5)
        tx_fn_tpc = Text("trianguloPorCuadrado()").scale(.4).next_to(gm_arr_0, UP, buff=.1)
        gm_sq_0 = Square(color=BLUE).scale(.8).next_to(gm_arr_0, RIGHT, buff=.5)

        self.play(Create(gm_tr_0))
        self.play(Write(gm_arr_0), Create(tx_fn_tpc))
        self.play(Create(gm_sq_0))

        gm_arr_1 = Arrow().scale(-2).shift(DOWN*3)
        gm_tr_1 = Triangle().scale(1.2).next_to(gm_arr_1, LEFT, buff=.5)
        tx_fn_cpt = Text("cuadradoPorTriangulo()").scale(.4).next_to(gm_arr_1, UP, buff=.1)
        gm_sq_1 = Square(color=BLUE).scale(.8).next_to(gm_arr_1, RIGHT, buff=.5)

        self.play(Create(gm_sq_1))
        self.play(Write(gm_arr_1), Create(tx_fn_cpt))
        self.play(Create(gm_tr_1))



