from background import generate_background
from palettes import get_palette
from PIL import ImageDraw
from shapes import draw_circles
from shapes import draw_stars
from shapes import draw_triangle
from shapes import draw_squiggle
from shapes import draw_diamonds
from shapes import draw_worm
from shapes import draw_raindrops
from shapes import draw_lines


def generate_artwork(vibe, complexity, save_path=None, size=(890, 697), selected_shapes=None):
    palette = get_palette(vibe)
    image = generate_background(size, palette)
    draw = ImageDraw.Draw(image)

    if selected_shapes is None:
        if vibe == "sunshine":
            selected_shapes = {"circles", "lines", "worm", "squiggle", "stars"}
        elif vibe == "dark":
            selected_shapes = {"lines", "triangle", "diamonds", "squiggle"}
        elif vibe == "colourful":
            selected_shapes = {"circles", "raindrop", "worm", "stars", "squiggle", "lines"}
        elif vibe == "forest":
            selected_shapes = {"triangle", "raindrop", "lines", "squiggle", "worm","triangle"}
        elif vibe == "pastel":
            selected_shapes = {"worm", "circles", "stars", "squiggle", "lines", "raindrop"}
        elif vibe == "beige":
            selected_shapes = {"worm", "circles", "stars"}
        else:
            selected_shapes = {"lines", "circles", "raindrop", "triangle", "diamonds", "squiggle"}

    if "circles" in selected_shapes:
        draw_circles(draw, palette, complexity, size)
    if "stars" in selected_shapes:
        draw_stars(draw, palette, complexity, size)
    if "triangle" in selected_shapes:
        draw_triangle(draw, palette, complexity, size)
    if "squiggle" in selected_shapes:
        draw_squiggle(draw, palette, complexity, size)
    if "diamonds" in selected_shapes:
        draw_diamonds(draw, palette, complexity, size)
    if "lines" in selected_shapes:
        draw_lines(draw, palette, complexity, size)
    if "raindrop" in selected_shapes:
        draw_raindrops(draw, palette, complexity, size)
    if "worm" in selected_shapes:
        draw_worm(image, draw, palette, complexity, size)

    if save_path:
        image.save(save_path)
    return image

