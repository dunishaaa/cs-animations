from manim import *


def normalPrime(n: int):
    l = [True for i in range(n + 1)]
    l[1] = False

    for i in range(1, n + 1):
        for j in range(2, i):
            if i == 1 or i % j == 0:
                l[i] = False
                break
    return l


def sievePrime(n: int):
    l = [True for i in range(n + 1)]
    l[1] = False
    return l


class Sieve(Scene):
    def construct(self):
        HEIGHT = 7
        WIDTH = 20
        gm_sq_grid = [
            Rectangle(
                width=0.7,
                height=1.0,
                color=BLUE,
                stroke_width=1.8,
                fill_color=BLUE,
                fill_opacity=0.6,
            )
            for i in range(WIDTH * HEIGHT)
        ]
        grid = VGroup(*gm_sq_grid).arrange_in_grid(HEIGHT, WIDTH)
        tx_sq_grid = [
            Integer(i + 1).move_to(sq.get_center()) for i, sq in enumerate(gm_sq_grid)
        ]
        grid.add(*tx_sq_grid)
        grid.scale(0.6)
        self.play(Create(grid), run_time=2)

        primes = normalPrime(HEIGHT * WIDTH)

        for i, sq in enumerate(gm_sq_grid):
            if primes[i + 1]:
                sq.set_color(GREEN).set_fill(GREEN)

        self.wait()
