from manim import *


class Intro(Scene):
    def construct(self):
        tx_que_funcion = Tex("¿Qué es una función?").scale(1.4)
        self.play(Write(tx_que_funcion))

        tx_que_funcion.generate_target()
        tx_que_funcion.target.to_edge(UP)
        tx_expl_funcion = Tex(
            "Una función es un bloque de código que realiza alguna operación" 
            ).scale(.8).next_to(tx_que_funcion.target, DOWN, buff=.5)
        self.play(MoveToTarget(tx_que_funcion))
        self.play(Write(tx_expl_funcion))

        #podemos tener la funcion trianguloPorCuadrado

        gm_arr_0 = Arrow().scale(2).next_to(tx_que_funcion, DOWN, buff=2)
        gm_tr_0 = Triangle(color=BLUE).scale(1.2).next_to(gm_arr_0, LEFT, buff=.5)
        tx_fn_tpc = Text("transformarACuadrado").scale(.7).next_to(tx_expl_funcion, DOWN, buff=.1)
        tx_fn_tpc_p = Text("transformarAcuadrado()",
                         t2c={'(':RED, ')': RED}
                         ).scale(.35).next_to(gm_arr_0, UP, buff=.1)
        tx_fn_tpc_ps = Text("transformarAcuadrado(triangulo)",
                         t2c={'(':RED, ')': RED, 'triangulo': BLUE},
                         t2w={'triangulo': BOLD}
                         ).scale(.32).next_to(gm_arr_0, UP, buff=.1)
        gm_sq_0 = Square(color=BLUE).scale(.8).next_to(gm_arr_0, RIGHT, buff=.5)

        self.play(Create(gm_tr_0))
        self.play(Write(gm_arr_0))
        self.play(Create(tx_fn_tpc))
        self.play(Transform(tx_fn_tpc, tx_fn_tpc_p))
        self.play(FocusOn(tx_fn_tpc_p[-2:]))

        tr_gb_0 = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_0, LEFT, buff=.5)

        del_gp_0 = VGroup(tx_que_funcion, tx_expl_funcion)
        tx_fn_con_params= Text("Con parámetros", color=BLUE_E).scale(.8).move_to(tx_expl_funcion.get_center())
        gp_funcion = VGroup(gm_arr_0, tr_gb_0, tx_fn_tpc_ps, gm_sq_0)
        box_params = SurroundingRectangle(gp_funcion, color=BLUE_E, buff=.2)
        self.play(FadeOut(del_gp_0, run_time=.2), FadeOut(tx_fn_tpc), FadeOut(tx_fn_tpc_p),Write(box_params), Create(tx_fn_con_params))
        gm_arr_param = CurvedArrow(tx_fn_con_params[-10:].get_center(), tx_fn_tpc_ps[-6:].get_center(), radius=10, color=BLUE_C).scale(.7)
        self.play(Create(gm_arr_param), Write(tx_fn_tpc_ps), run_time=.5)
        self.play(Transform(gm_tr_0, gm_sq_0))

        tx_fn_sin_params= Text("Sin parámetros", color=GREEN_E).scale(.8).next_to(gm_arr_0, DOWN, buff=1.2)
        gm_arr_1 = Arrow().scale(2).next_to(tx_fn_sin_params, DOWN, buff=1)
        tx_fn_sU = Text("dameUno()", t2c={'(':RED, ')': RED}).scale(.4).next_to(gm_arr_1, UP, buff=.1)
        tx_uno = Text("1", color="BLUE").move_to(gm_arr_1.get_center())
        tx_uno.generate_target()
        tx_uno.target.next_to(gm_arr_1, RIGHT, buff=1)

        tr_gb = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_1, LEFT, buff=.5)

        gm_sq_1 = Square(color=BLACK).scale(.8).next_to(gm_arr_1, RIGHT, buff=.5)
        gp_funcion_sin_params = VGroup(gm_sq_1, tr_gb, gm_arr_1, tx_fn_sU, tx_uno.target)
        box_sin_params = SurroundingRectangle(gp_funcion_sin_params, color=GREEN_E)

        self.play(Write(tx_fn_sin_params), Write(box_sin_params))
        self.play(Create(gm_arr_1), Create(tx_fn_sU))
        self.play(Write(tx_uno))
        self.play(MoveToTarget(tx_uno))

        self.play(
            FadeOut(gp_funcion_sin_params), 
            FadeOut(gp_funcion), 
            FadeOut(box_params),
            FadeOut(box_sin_params),
            FadeOut(tx_fn_sin_params),
            FadeOut(tx_fn_con_params),
            FadeOut(gm_arr_param),
            run_time=.2
            )
        self.clear()
        self.wait()

class MasEjemplosFunciones(Scene):
    def construct(self):
        tx_title = Tex("Más funciones con parámetros",).scale(1.4).to_corner(UP)
        self.play(Write(tx_title))
        tx_fn_suma = Text("sumaDosNumeros(x, y)", 
                          t2c={'x': BLUE, 'y':RED},
                          t2w={'x': BOLD, 'y':BOLD},
                          font_size=20 
                          ).next_to(tx_title, DOWN, buff=1)
        listing = Code(
            "sumaDosNumeros.js",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="Javascript",
        )
        box_fn = SurroundingRectangle(tx_fn_suma, color=YELLOW_E, buff=.3)
        listing.next_to(box_fn, DOWN, buff=1)
        self.play(Write(tx_fn_suma), Write(box_fn))
        self.play(Create(listing), run_time=1)
        gm_arr_0 = Arrow(color=BLUE).scale(.7).next_to(box_fn.get_corner(UL), LEFT, buff=.3)
        gm_arr_1 = Arrow(color=RED).scale(.7).next_to(box_fn.get_corner(DL), LEFT, buff=.3)
        tx_x = Tex("4", color=BLUE).next_to(gm_arr_0, LEFT, buff=.5)
        tx_y = Tex("5", color=RED).next_to(gm_arr_1, LEFT, buff=.5)
        self.play(Create(gm_arr_0), Create(gm_arr_1))
        self.play(Write(tx_x), Write(tx_y))
        tx_op_fn = Text("4 + 5 = 9", t2c={'4':BLUE, '5':RED, '9':YELLOW_E}, font_size=25
                         ).move_to(tx_fn_suma.get_center())
        gp_nums = VGroup(tx_x, tx_y)
        copy_nums = gp_nums.copy()
        self.play(Create(copy_nums, run_time=.1), FadeOut(tx_fn_suma),Transform(gp_nums, tx_op_fn))
        self.wait(.5)
        gm_arr_2 = Arrow(color=YELLOW_E).scale(.7).next_to(box_fn, RIGHT, buff=.3)
        tx_res_fn = Text('9', color=YELLOW_E).next_to(gm_arr_2,RIGHT, buff=.5)
        self.play(FadeOut(gp_nums),Transform(tx_op_fn, tx_res_fn), FadeIn(tx_fn_suma), Write(gm_arr_2), run_time=2)


        



