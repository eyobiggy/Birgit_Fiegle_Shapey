from background import generate_background
from palettes import get_palette
from PIL import ImageDraw
from shapes import draw_circles
from shapes import draw_stars
from shapes import draw_triangle
from shapes import draw_worm
from shapes import draw_raindrops
from shapes import draw_lines

def generate_artwork(vibe, complexity, save_path=None, size=(800, 800), selected_shapes=None):
    palette = get_palette(vibe)
    image = generate_background(size, palette)
    draw = ImageDraw.Draw(image)

    if selected_shapes is None:
        selected_shapes = {"circles", "stars", "triangle", "worm", "raindrops", "lines"}

    if "circles" in selected_shapes:
        draw_circles(draw, palette, complexity, size)
    if "stars" in selected_shapes:
        draw_stars(draw, palette, complexity, size)
    if "triangle" in selected_shapes:
        draw_triangle(draw, palette, complexity, size)
    if "worm" in selected_shapes:
        draw_worm(draw, palette, complexity, size)
    if "raindrops" in selected_shapes:
        draw_raindrops(draw, palette, complexity, size)
    if "lines" in selected_shapes:
        draw_lines(draw, palette, complexity, size)

    if save_path:
        image.save(save_path)
    return image

