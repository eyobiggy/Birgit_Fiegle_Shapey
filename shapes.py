import random
import math
from PIL import ImageDraw

def draw_circles(draw, palette, complexity, size):
    width, height = size
    count = complexity * 10  # Adjust multiplier as needed

    for _ in range(count):
        radius = random.randint(10, int(100 / complexity))
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = random.choice(palette)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=None)

def draw_star(draw, cx, cy, r, color):
    points = []
    for i in range(10):
        angle = math.radians(i * 36)  # 360 / 10
        radius = r if i % 2 == 0 else r * 0.5
        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius
        points.append((x, y))
    draw.polygon(points, fill=color)

def draw_stars(draw, palette, complexity, size):
    for _ in range(complexity * 5):
        cx = random.randint(0, size[0])
        cy = random.randint(0, size[1])
        r = random.randint(20, 60)
        color = random.choice(palette)
        draw_star(draw, cx, cy, r, color)

def draw_triangle(draw, palette, complexity, size):
    for _ in range(complexity * 6):
        x1 = random.randint(0, size[0])
        y1 = random.randint(0, size[1])
        x2 = x1 + random.randint(-100, 100)
        y2 = y1 + random.randint(-100, 100)
        x3 = x1 + random.randint(-100, 100)
        y3 = y1 + random.randint(-100, 100)
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=random.choice(palette))

def draw_worm(draw, palette, complexity, size):
    for _ in range(complexity * 3):
        points = []
        x, y = random.randint(0, size[0]), random.randint(0, size[1])
        for _ in range(random.randint(10, 30)):
            dx = random.randint(-20, 20)
            dy = random.randint(-20, 20)
            x += dx
            y += dy
            points.append((x, y))
        color = random.choice(palette)
        draw.line(points, fill=color, width=random.randint(3, 8), joint="curve")

def draw_raindrop(draw, cx, cy, size, color):
    # Teardrop shape
    w = size
    h = size * 1.5
    drop = [
        (cx, cy - h / 2),
        (cx + w / 2, cy),
        (cx, cy + h / 2),
        (cx - w / 2, cy)
    ]
    draw.polygon(drop, fill=color)

def draw_raindrops(draw, palette, complexity, size):
    for _ in range(complexity * 8):
        cx = random.randint(0, size[0])
        cy = random.randint(0, size[1])
        r = random.randint(10, 40)
        color = random.choice(palette)
        draw_raindrop(draw, cx, cy, r, color)