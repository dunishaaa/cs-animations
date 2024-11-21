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
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False
    return is_prime


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

        # primes = normalPrime(HEIGHT * WIDTH)
        primes = sievePrime(HEIGHT * WIDTH)

        n: int = HEIGHT * WIDTH

        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = False
        is_prime[1] = False
        rt = 0.7
        curr_counter = 4
        for i in range(2, n + 1):
            if is_prime[i]:
                if curr_counter > 0:
                    self.play(gm_sq_grid[i - 1].animate.set_color(YELLOW), run_time=rt)
                else:
                    self.play(gm_sq_grid[i - 1].animate.set_color(YELLOW), run_time=0.3)
                counter = 5
                for j in range(i * i, n + 1, i):
                    if is_prime[j]:
                        is_prime[j] = False
                        if counter >= 0:
                            self.play(
                                Succession(
                                    Indicate(gm_sq_grid[j - 1], color=WHITE),
                                    gm_sq_grid[j - 1].animate.set_color(RED),
                                ),
                                run_time=1,
                            )
                            counter -= 1
                        else:
                            self.play(
                                Succession(
                                    Indicate(gm_sq_grid[j - 1], color=WHITE),
                                    gm_sq_grid[j - 1].animate.set_color(RED),
                                ),
                                run_time=0.1,
                            )
                self.play(gm_sq_grid[i - 1].animate.set_color(GREEN), run_time=rt)

        self.wait()
