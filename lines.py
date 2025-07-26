import random

def draw_lines(draw, palette, complexity, size):
    width, height = size
    count = complexity * 7

    for _ in range(count):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        color = random.choice(palette)
        draw.line((x1, y1, x2, y2), fill=color, width=random.randint(1, 4))