import math


def fig(figure_type, **dan):
    if figure_type == "rhombus":
        return dan["d1"] * dan["d2"] / 2
    elif figure_type == 'square':
        return dan["a"] ** 2
    elif figure_type == 'trapezoids':
        return (1 / 2) * ((dan["a"] + dan["b"]) * dan["h"])
    elif figure_type == 'circle':
        return math.pi * (dan["r"] ** 2)
    elif figure_type == 'unknown':
        return "invalid data"


print(fig("rhombus", d1=10, d2=8))
print(fig('square', a=5))
print(fig('trapezoids', a=12, b=3, h=6))
print(fig('circle', r=18))
print(fig('unknown', a=1, b='2', c='3'))
