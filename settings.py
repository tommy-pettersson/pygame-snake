from math import floor

def init():
    global width, height
    global cols, rows
    global w
    global grid

    width = 600
    height = 600
    cols = 20
    rows = cols
    w = floor(width / cols)
    grid = make_2D_array(cols, rows)


def make_2D_array(cols, rows):
    array = [n for n in range(cols)]
    for i, _ in enumerate(array):
        array[i] = [n for n in range(rows)]
    return array
