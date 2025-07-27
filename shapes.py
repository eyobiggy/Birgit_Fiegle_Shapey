import random
import math
from PIL import ImageDraw, Image

def hex_to_rgba(hex_color, alpha=255):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b, alpha)

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

def draw_circles(draw, palette, complexity, size):
    width, height = size
    count = int((complexity ** 2) * 1.5)  # Adjust multiplier as needed

    for _ in range(count):
        radius = random.randint(10, int(150 / complexity))
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = random.choice(palette)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=None)

def draw_star(draw, cx, cy, size, color):
    """
    Draws a 5-pointed star centered at (cx, cy) with a given size and random rotation.
    """
    outer_radius = size / 2
    inner_radius = outer_radius * 0.5
    angle_offset = math.radians(random.uniform(0, 360))  # random rotation in radians

    points = []
    for i in range(10):  # 5 outer + 5 inner points
        angle = angle_offset + i * math.pi / 5  # 36 degrees step
        r = outer_radius if i % 2 == 0 else inner_radius
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append((x, y))

    draw.polygon(points, fill=color)

def draw_stars(draw, palette, complexity, size):
    for _ in range(int(complexity ** 1.7) * 2):
        cx = random.randint(0, size[0])
        cy = random.randint(0, size[1])
        r = random.randint(10, 100)
        color = random.choice(palette)
        draw_star(draw, cx, cy, r, color)

def draw_triangle(draw, palette, complexity, size):
    for _ in range(int((complexity ** 2) * 1.5)):
        x1 = random.randint(0, size[0])
        y1 = random.randint(0, size[1])
        x2 = x1 + random.randint(-150, 150)
        y2 = y1 + random.randint(-150, 150)
        x3 = x1 + random.randint(-150, 150)
        y3 = y1 + random.randint(-150, 150)
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=random.choice(palette))

def draw_squiggle(draw, palette, complexity, size):
    for _ in range(int(complexity ** 1.3)):
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

def draw_worm(image, draw, palette, complexity, size):
    for _ in range(max(1, int(complexity * 0.6))):
        cx = random.randint(100, size[0] - 100)
        cy = random.randint(100, size[1] - 100)
        length = random.randint(100, 400)
        curves = random.randint(1, 3)
        amplitude = random.randint(20, 50)
        direction = random.choice(["horizontal", "vertical"])
        color = hex_to_rgba(random.choice(palette), alpha=150)
        thickness = random.randint(10, 50)

        # Prepare the worm path
        points = []
        for i in range(100):
            t = i / 99
            angle = t * curves * math.pi * 2
            offset = math.sin(angle) * amplitude
            if direction == "horizontal":
                x = cx + t * length
                y = cy + offset
            else:
                x = cx + offset
                y = cy + t * length
            points.append((x, y))

        # Draw overlapping circles along the path
        worm_overlay = Image.new("RGBA", size, (0, 0, 0, 0))
        worm_draw = ImageDraw.Draw(worm_overlay)

        radius = thickness // 2
        for (x, y) in points:
            worm_draw.ellipse(
                [x - radius, y - radius, x + radius, y + radius],
                fill=color
            )

        # Paste onto main image
        image.paste(worm_overlay, (0, 0), worm_overlay)

def draw_diamond(draw, cx, cy, size, color):
    w = size
    h = size * 1.5
    drop = [
        (cx, cy - h / 2),
        (cx + w / 2, cy),
        (cx, cy + h / 2),
        (cx - w / 2, cy)
    ]
    draw.polygon(drop, fill=color)

def draw_diamonds(draw, palette, complexity, size):
    for _ in range(int((complexity ** 2) * 1.5)):
        cx = random.randint(0, size[0])
        cy = random.randint(0, size[1])
        r = random.randint(8, 50)
        color = random.choice(palette)
        draw_diamond(draw, cx, cy, r, color)

def draw_raindrop(draw, cx, cy, size, color):
    """
    Draw a 💧-shaped raindrop using two straight lines and a circular arc.
    cx, cy = center of the circle at the bottom
    size = width of the circle (diameter)
    color = fill color
    """
    radius = size / 2
    circle_center = (cx, cy)
    angle_degrees = 18.35  # half of 36.7°

    # Calculate points where lines touch the circle (points B and C)
    angle_radians = math.radians(angle_degrees)
    dx = math.sin(angle_radians) * radius
    dy = math.cos(angle_radians) * radius

    bx = cx + dx
    by = cy - dy
    cx_ = cx - dx
    cy_ = by  # same height as B

    # Tip point A
    tip_height = cy - radius - radius * 0.6  # slightly above the circle
    ax = cx
    ay = tip_height

    # Create path: A -> B -> arc from B to C -> C -> back to A
    path = [(ax, ay), (bx, by)]

    # Draw arc (approximated with points)
    steps = 30
    for i in range(steps + 1):
        theta = math.pi * (i / steps)  # From 0 to π
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        path.append((x, y))

    path.append((cx_, cy_))
    path.append((ax, ay))  # close path

    draw.polygon(path, fill=color)


def draw_raindrops(draw, palette, complexity, size):
    for _ in range(int((complexity ** 2) * 1.5)):
        cx = random.randint(0, size[0])
        cy = random.randint(0, size[1])
        r = random.randint(10, 80)
        color = random.choice(palette)
        draw_raindrop(draw, cx, cy, r, color)