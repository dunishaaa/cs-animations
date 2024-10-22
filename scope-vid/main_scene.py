from manim import *
from random import randint


class Intro(Scene):
    def construct(self):
        tx_que_funcion = Tex("¿Qué es una función?").scale(1.4)
        self.play(Write(tx_que_funcion))

        tx_que_funcion.generate_target()
        tx_que_funcion.target.to_edge(UP)
        tx_expl_funcion = (
            Tex("Una función es un bloque de código que realiza alguna operación")
            .scale(0.8)
            .next_to(tx_que_funcion.target, DOWN, buff=0.5)
        )
        self.play(MoveToTarget(tx_que_funcion))
        self.play(Write(tx_expl_funcion))

        # podemos tener la funcion trianguloPorCuadrado

        gm_arr_0 = Arrow().scale(2).next_to(tx_que_funcion, DOWN, buff=2)
        gm_tr_0 = Triangle(color=BLUE).scale(1.2).next_to(gm_arr_0, LEFT, buff=0.5)
        tx_fn_tpc = (
            Text("transformarACuadrado")
            .scale(0.7)
            .next_to(tx_expl_funcion, DOWN, buff=0.1)
        )
        tx_fn_tpc_p = (
            Text("transformarAcuadrado()", t2c={"(": RED, ")": RED})
            .scale(0.35)
            .next_to(gm_arr_0, UP, buff=0.1)
        )
        tx_fn_tpc_ps = (
            Text(
                "transformarAcuadrado(triangulo)",
                t2c={"(": RED, ")": RED, "triangulo": BLUE},
                t2w={"triangulo": BOLD},
            )
            .scale(0.32)
            .next_to(gm_arr_0, UP, buff=0.1)
        )
        gm_sq_0 = Square(color=BLUE).scale(0.8).next_to(gm_arr_0, RIGHT, buff=0.5)

        self.play(Create(gm_tr_0))
        self.play(Write(gm_arr_0))
        self.play(Create(tx_fn_tpc))
        self.play(Transform(tx_fn_tpc, tx_fn_tpc_p))
        self.play(FocusOn(tx_fn_tpc_p[-2:]))

        tr_gb_0 = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_0, LEFT, buff=0.5)

        del_gp_0 = VGroup(tx_que_funcion, tx_expl_funcion)
        tx_fn_con_params = (
            Text("Con parámetros", color=BLUE_E)
            .scale(0.8)
            .move_to(tx_expl_funcion.get_center())
        )
        gp_funcion = VGroup(gm_arr_0, tr_gb_0, tx_fn_tpc_ps, gm_sq_0)
        box_params = SurroundingRectangle(gp_funcion, color=BLUE_E, buff=0.2)
        self.play(
            FadeOut(del_gp_0, run_time=0.2),
            FadeOut(tx_fn_tpc),
            FadeOut(tx_fn_tpc_p),
            Write(box_params),
            Create(tx_fn_con_params),
        )
        gm_arr_param = CurvedArrow(
            tx_fn_con_params[-10:].get_center(),
            tx_fn_tpc_ps[-6:].get_center(),
            radius=10,
            color=BLUE_C,
        ).scale(0.7)
        self.play(Create(gm_arr_param), Write(tx_fn_tpc_ps), run_time=0.5)
        self.play(Transform(gm_tr_0, gm_sq_0))

        tx_fn_sin_params = (
            Text("Sin parámetros", color=GREEN_E)
            .scale(0.8)
            .next_to(gm_arr_0, DOWN, buff=1.2)
        )
        gm_arr_1 = Arrow().scale(2).next_to(tx_fn_sin_params, DOWN, buff=1)
        tx_fn_sU = (
            Text("dameUno()", t2c={"(": RED, ")": RED})
            .scale(0.4)
            .next_to(gm_arr_1, UP, buff=0.1)
        )
        tx_uno = Text("1", color="BLUE").move_to(gm_arr_1.get_center())
        tx_uno.generate_target()
        tx_uno.target.next_to(gm_arr_1, RIGHT, buff=1)

        tr_gb = Triangle(color=BLACK).scale(1.2).next_to(gm_arr_1, LEFT, buff=0.5)

        gm_sq_1 = Square(color=BLACK).scale(0.8).next_to(gm_arr_1, RIGHT, buff=0.5)
        gp_funcion_sin_params = VGroup(
            gm_sq_1, tr_gb, gm_arr_1, tx_fn_sU, tx_uno.target
        )
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
            run_time=0.2,
        )
        self.clear()
        self.wait()


class MasEjemplosFunciones(Scene):
    def construct(self):
        tx_title = (
            Tex(
                "Más funciones con parámetros",
            )
            .scale(1.4)
            .to_corner(UP)
        )
        self.play(Write(tx_title))
        tx_fn_suma = Text(
            "sumaDosNumeros(x, y)",
            t2c={"x": BLUE, "y": RED},
            t2w={"x": BOLD, "y": BOLD},
            font_size=20,
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
        box_fn = SurroundingRectangle(tx_fn_suma, color=YELLOW_E, buff=0.3)
        listing.next_to(box_fn, DOWN, buff=1)
        self.play(Write(tx_fn_suma), Write(box_fn))
        self.play(Create(listing), run_time=1)
        gm_arr_0 = (
            Arrow(color=BLUE).scale(0.7).next_to(box_fn.get_corner(UL), LEFT, buff=0.3)
        )
        gm_arr_1 = (
            Arrow(color=RED).scale(0.7).next_to(box_fn.get_corner(DL), LEFT, buff=0.3)
        )
        tx_x = Tex("4", color=BLUE).next_to(gm_arr_0, LEFT, buff=0.5)
        tx_y = Tex("5", color=RED).next_to(gm_arr_1, LEFT, buff=0.5)
        self.play(Create(gm_arr_0), Create(gm_arr_1))
        self.play(Write(tx_x), Write(tx_y))
        tx_op_fn = Text(
            "4 + 5 = 9", t2c={"4": BLUE, "5": RED, "9": YELLOW_E}, font_size=25
        ).move_to(tx_fn_suma.get_center())
        gp_nums = VGroup(tx_x, tx_y)
        copy_nums = gp_nums.copy()
        self.play(
            Create(copy_nums, run_time=0.1),
            FadeOut(tx_fn_suma),
            Transform(gp_nums, tx_op_fn),
        )
        self.wait(0.5)
        gm_arr_2 = Arrow(color=YELLOW_E).scale(0.7).next_to(box_fn, RIGHT, buff=0.3)
        tx_res_fn = Text("9", color=YELLOW_E).next_to(gm_arr_2, RIGHT, buff=0.5)
        self.play(
            FadeOut(gp_nums),
            Transform(tx_op_fn, tx_res_fn),
            FadeIn(tx_fn_suma),
            Write(gm_arr_2),
            run_time=2,
        )


def mv_dot(dot: Dot, og_line: Line, vlt: ValueTracker):
    start = og_line.get_start()[0]
    end = og_line.get_end()[0]
    vl = vlt.get_value()
    if start <= vl <= end: 
        dot.set_x(vlt.get_value())

def hp_set_opacity(obj: VMobject, og_line: Line, vlt: ValueTracker):
    vl = vlt.get_value()
    start = og_line.get_start()[0]
    end = og_line.get_end()[0]
    if start < vl > end: 
        obj.set_opacity(.2)
#        obj.set_stroke(width=2)
    else:
        obj.set_opacity(1)
#        obj.set_stroke(width=6)
        

class DetallesScope(Scene):
    def construct(self):
        self.next_section(skip_animations=False)
        tx_title = Text(
            "¿Qué es el scope(o alcance)?",
            t2w={"scope":BOLD},
            )
        self.play(Write(tx_title))
        self.play(Unwrite(tx_title), run_time=.3)

        tx_def = Text(
            "El scope determina que partes del programa pueden ser usadas, cuando podemos definir, redefinir y usar una variable sin conflictos",
            width=10,
#            t2c={"scope": BLUE_E, "definir": GREEN_A, "redefinir": GREEN_A, "usar": GREEN_A}
        )
        self.play(Write(tx_def))

        tx_brackets = Text(
                        "Se pude delimitar con {} o indentando..."
                    ).to_edge(UP, buff=.7)
        
        self.play(Write(tx_brackets))

        cb_js =Code(
                    "scope.js",
                    tab_width=4,
                    background_stroke_width=1,
                    background_stroke_color=WHITE,
                    style=Code.styles_list[15],
                    language="Javascript",
                ).scale(.5).next_to(tx_brackets, DOWN, buff=1).shift(LEFT)
        
        cb_py =Code(
                    "pyex.py",
                    tab_width=4,
                    background_stroke_width=1,
                    background_stroke_color=WHITE,
                    style=Code.styles_list[15],
                    language="Python",
                ).scale(.5).next_to(cb_js, RIGHT, buff=1)

        self.play(Write(cb_js), Write(cb_py))
        

        

class Scope(Scene):
    def construct(self):

        nm = NumberPlane().add_coordinates()
        #self.add(nm)

        color_palette = [BLUE, RED, PURPLE, YELLOW_E, ORANGE]
        lines_texts = ["Program", "main()", "if", "var_y", "for"]


        gm_ln_ogs = [] 
        #Initial guide-lines
        gm_ln_ogs.append(Line(start=[-6, 3.7, 0], end=[6, 3.7, 0], stroke_width=7))
        gm_ln_ogs.append(Line(start=[-5.7, 3, 0], end=[5.7,3 ,0],stroke_width=7))
        gm_ln_ogs.append(Line(start=[-5.0, 2.3, 0], end=[-0.2, 2.3,0],stroke_width=7))
        gm_ln_ogs.append(Line(start=[0.1, 2.3, 0], end=[5.7, 2.3, 0],stroke_width=7))
        gm_ln_ogs.append(Line(start=[3, 1.6, 0], end=[4.5, 1.6,0],stroke_width=7))



        #Dots to begining of guide-lines
        gm_dots = [
            Dot(gm_ln_ogs[i].get_start(), color=color_palette[i]).scale(1.3) 
            for i in range(len(color_palette))
        ]

        #Color line redraw
        gm_ln_colored = [
            always_redraw(
                lambda i=i: Line(
                    start=gm_ln_ogs[i].get_start(), end=gm_dots[i].get_center(), color=color_palette[i], stroke_width=7
                    )
                )
                for i in range(len(color_palette))
            ]

        gm_ln_cb = [] 
        gm_ln_cb.append(Line(start=[-6.4, 2.0, 0],  end=[-6.4, -3.0, 0], color=BLUE, stroke_width=4))
        gm_ln_cb.append(Line(start=[-6.2, 1.8, 0],  end=[-6.2, -2.85, 0], color=RED, stroke_width=4))
        gm_ln_cb.append(Line(start=[-6.0, 1.4, 0],  end=[-6.0, -0.1, 0], color=PURPLE, stroke_width=4))
        gm_ln_cb.append(Line(start=[-6.0, -0.3, 0], end=[-6.0, -2.85, 0], color=YELLOW_E, stroke_width=4))
        gm_ln_cb.append(Line(start=[-5.8, -1.6, 0], end=[-5.8, -2.6, 0], color=ORANGE, stroke_width=4))



        gm_ln_ini_color_lines = [
            Line(start=[-6, 1, 0], end=[-6, -2, 0], stroke_width=10, color=color_palette[i]).scale(1.5)
            for i in range(len(color_palette))
        ]
        tx_program_parts = [
            Text(lines_texts[i], color=color_palette[i], slant=ITALIC, font_size=20).next_to(gm_ln_ini_color_lines[i], RIGHT, buff=.2)
            for i in range(len(lines_texts))
        ]



        codeB_scope= Code(
            "scope.js",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            style=Code.styles_list[15],
            language="Javascript",
        ).scale(.7).to_edge(LEFT, buff=.6).shift(DOWN*.5).scale(1.1)
        displace = ORIGIN - codeB_scope.get_center() + DOWN * 1.3

        codeB_scope.shift(displace)
        for ln in gm_ln_cb:
            ln.scale(1.1).shift(displace)


        self.add(codeB_scope)

        self.play(*[Write(og_line) for og_line in gm_ln_ogs])
        self.play(*[Write(dot) for dot in gm_dots])
        self.add(*gm_ln_colored)




        for i in range(len(gm_ln_cb)):
            self.play(Create(tx_program_parts[i]), Create(gm_ln_ini_color_lines[i]))
            tx_program_parts[i].generate_target()
            tx_program_parts[i].target.next_to(gm_dots[i], DOWN, buff=.1)
            self.play(MoveToTarget(tx_program_parts[i]), ReplacementTransform(gm_ln_ini_color_lines[i], gm_ln_cb[i]))
            self.add(gm_ln_cb[i])

        for i in range(len(tx_program_parts)):
            tx_program_parts[i].add_updater(lambda _, i=i: tx_program_parts[i].next_to(gm_dots[i], DOWN, buff=.1))

        self.next_section()

        vlt_program_lifetime = ValueTracker(gm_ln_ogs[0].get_start()[0]-.5)
        
        for i in range(len(gm_dots)):
            gm_dots[i].add_updater(
                    lambda _, i=i: 
                        mv_dot(gm_dots[i], gm_ln_ogs[i], vlt_program_lifetime)
                )
        
        gm_ln_dh = always_redraw(
            lambda:
                DashedLine(
                    start=[vlt_program_lifetime.get_value(), 5, 0], 
                    end=[vlt_program_lifetime.get_value(), -5, 0], 
                    stroke_width=10,
                    dash_length=.3,
                    dashed_ratio=.5,
                    color=GREEN
                ).set_opacity(.7)
        )
        self.play(Write(gm_ln_dh), run_time=1)
        #set opacity
        for i in range(len(gm_dots)):
            gm_ln_cb[i].add_updater(
                lambda _, i=i:
                    hp_set_opacity(gm_ln_cb[i], gm_ln_ogs[i], vlt_program_lifetime)
            )

            gm_dots[i].add_updater(
                lambda _, i=i:
                    hp_set_opacity(gm_dots[i], gm_ln_ogs[i], vlt_program_lifetime)
            )
            gm_ln_colored[i].add_updater(
                lambda _, i=i:
                    hp_set_opacity(gm_ln_colored[i], gm_ln_ogs[i], vlt_program_lifetime)
            )
            tx_program_parts[i].add_updater(
                lambda _, i=i:
                    hp_set_opacity(tx_program_parts[i], gm_ln_ogs[i], vlt_program_lifetime)
            )
            gm_ln_ogs[i].add_updater(
                lambda _, i=i:
                    hp_set_opacity(gm_ln_ogs[i], gm_ln_ogs[i], vlt_program_lifetime)
            )

        

        self.play(vlt_program_lifetime.animate.set_value(10), run_time=14,rate_func=linear)
        self.wait(2)


    

    

import random
def hola(start, end, color):
    return Line(start=start, end=end, color=color)

class Test(Scene):
        
    def construct(self):
        num = 5
        color_palette = [BLUE, RED, PURPLE, YELLOW_E, ORANGE]
        names= ['BLUE', 'RED', 'PURPLE', 'YELLOW_E', 'ORANGE']
        vt = ValueTracker(-5)

        gm_dots = [Dot([-5, 2-i, 0], color=color_palette[i]) for i in range(num)]
        

        speed = [.35, .4, .01, .6, .21]
        for i in range(len(gm_dots)):
            gm_dots[i].add_updater(lambda dot=gm_dots[i], i=i: move(dot, speed[i], names[i]))
        


        self.add(*gm_dots)
        gm_lines = [
            always_redraw(
                lambda i=i:
                hola([-5, 2-i, 0], gm_dots[i].get_center(), color_palette[i])
            ) for i in range(num)
        ]
        
        
        self.add(*gm_lines)

        self.play(vt.animate.set_value(5), run_time=5 )

def rd_ln_col(st, end, col ):
    return Line(start=st, end=end, stroke_width=7, color=col )

def mv_dot(dot: Dot, og_line: Line, vt: ValueTracker):
    st = og_line.get_start()[0]
    end = og_line.get_end()[0]
    cur = vt.get_value() 
    if st <= cur < end:
        dot.set_x(cur)


def set_opacityP(dot: Dot, og_line: Line, obj: VMobject, vt: ValueTracker):
    st = og_line.get_start()[0]
    end = og_line.get_end()[0]
    cur = dot.get_center()[0]
    val = vt.get_value()
    if st <= val <= end:
        obj.set_opacity(1)
    else:
        obj.set_opacity(.2)
            

class Test3(Scene):
    def construct(self):
        num = 5
        color_palette = [BLUE, RED, PURPLE, YELLOW_E, ORANGE]
        names= ['BLUE', 'RED', 'PURPLE', 'YELLOW_E', 'ORANGE']
        vt = ValueTracker(-5)
        gm_ln_dh = always_redraw(
            lambda:
                DashedLine(
                    start=[vt.get_value(), 5, 0], 
                    end=[vt.get_value(), -5, 0], 
                    stroke_width=10,
                    dash_length=.3,
                    dashed_ratio=.5,
                    color=GREEN
                ).set_opacity(.7)
        )
        rnd_start = [-4, -2, -1.3, -5, -3]
        rnd = [1, 5, 2.6, 4.5, 3]
        gm_ln_og = [
            Line(start=[rnd_start[i], 2-i, 0], end=[rnd[i], 2-i, 0], stroke_width=7).set_opacity(.2)
            for i in range(num)
        ]
        gm_dots = [
            Dot([rnd_start[i], 2-i, 0], color=color_palette[i], radius=.15)
            for i in range(num)
        ]
        gm_ln_colors = [
            always_redraw(lambda i = i:
                rd_ln_col([rnd_start[i], 2-i, 0], gm_dots[i].get_center(), color_palette[i])
            )
            for i in range(num)
        ]

        
        self.add(*gm_ln_colors)
        self.play(
            *[Create(line, run_time=4) for line in gm_ln_og],
            Succession(
                *[Write(dot) for dot in gm_dots],
                run_time=2
            ),
        )
        self.wait(.7)

        self.play(Write(gm_ln_dh, run_time=1.5))

        for i in range(num):
            gm_dots[i].add_updater(
                lambda _, i=i:
                    mv_dot(gm_dots[i], gm_ln_og[i], vt)
            )
            #opacity
            gm_dots[i].add_updater(
                lambda _, i=i:
                    set_opacityP(gm_dots[i], gm_ln_og[i], gm_dots[i], vt)
            )

            gm_ln_colors[i].add_updater(
                lambda _, i=i:
                    set_opacityP(gm_dots[i], gm_ln_og[i], gm_ln_colors[i], vt)
            )

        self.play(vt.animate.set_value(6), run_time=6, rate_func=linear)
    
