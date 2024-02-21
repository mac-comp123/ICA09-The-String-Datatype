"""
Draw fractal

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""

import turtle


def draw_fractal(tur: turtle, l_system: str, angle: float, step_size: float):
    """
    Using the passed turtle, draw the l-system with the angle and step_size
    """
    assert isinstance(tur, turtle.Turtle)
    assert type(l_system) is str
    assert type(angle) in [int, float]
    assert type(step_size) in [int, float]

    for c in l_system:
        if c == 'F':
            tur.forward(step_size)
        elif c == 'f':
            tur.up()
            tur.forward(step_size)
            tur.down()
        elif c == '-':
            tur.right(angle)
        elif c == '+':
            tur.left(angle)
        elif c == '|':
            tur.left(180)
