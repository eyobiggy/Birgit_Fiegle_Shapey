import pygame
import random
import sys
import os
import time
from main import generate_artwork
from io import BytesIO
from PIL import Image

pygame.init()

start_bg = pygame.image.load(os.path.join("assets", "start_bg.png"))
display_bg = pygame.image.load(os.path.join("assets", "display_bg.png"))

# Constants
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font("assets/spacemono_font.ttf", 24)
TEXT_COLOR = (31, 26, 22)
BG_COLOR = (240, 240, 240)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapey - your fun background generator")

# States
STATE_START = "start"
STATE_DISPLAY = "display"
current_state = STATE_START

# Settings
vibes = ["sunshine", "dark", "colourful", "pastel", "beige", "ocean","forest"]
selected_vibe_index = 0
complexity = 3

# Image holder
generated_image = None
generated_surface = None

save_message = ""
save_message_timer = 0

dropdown_open = False
dragging_slider = False
surprise_active = False

def ask_save_path_safe():
    # Choose a base folder — you can also use "~/Desktop" or "~/Documents"
    base_folder = os.path.expanduser("~/Pictures/GeneratedArt")
    os.makedirs(base_folder, exist_ok=True)  # Create folder if it doesn't exist

    # Generate a unique filename based on timestamp
    timestamp = int(time.time())
    filename = f"generated_image_{timestamp}.png"

    # Full path to save image
    return os.path.join(base_folder, filename)


def pil_to_surface(pil_image):
    """Convert PIL image to Pygame surface."""
    with BytesIO() as buffer:
        pil_image.save(buffer, format="PNG")
        buffer.seek(0)
        return pygame.image.load(buffer)


def draw_text(text, x, y):
    label = FONT.render(text, True, TEXT_COLOR)
    screen.blit(label, (x, y))

def draw_start_block(screen, screen_size):
    width, height = screen_size

    # Margins from each side (10% of width/height)
    margin_x = int(width * 0.1)
    margin_y = int(height * 0.1)

    # Block dimensions
    block_width = width - 2 * margin_x
    block_height = height - 2 * margin_y

    # Block position
    block_x = margin_x
    block_y = margin_y

    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)

    # Shadow colors
    shadow_color = (110, 67, 28)
    border_color = (110, 67, 28)
    fill_color = (255, 237, 212)

    # --- Draw shadow (right and bottom only) ---
    shadow_thickness = 10
    # Bottom shadow
    pygame.draw.rect(screen, shadow_color,
        pygame.Rect(block_x + shadow_thickness, block_y + block_height, block_width, shadow_thickness))
    # Right shadow
    pygame.draw.rect(screen, shadow_color,
        pygame.Rect(block_x + block_width, block_y + shadow_thickness, shadow_thickness, block_height))

    # --- Draw block background ---
    pygame.draw.rect(screen, fill_color, block_rect)

    # --- Draw normal outline (top & left) ---
    pygame.draw.rect(screen, border_color, block_rect, 3)

def draw_message_box(message, filepath, x, y, width, height):

    small_font = pygame.font.Font("assets/spacemono_font.ttf", 16)
    # Colors same as buttons
    base_color = (255, 237, 212)
    border_color = (110, 67, 28)
    shadow_color = (110, 67, 28)
    shadow_thickness = 5

    # Draw shadow (bottom and right)
    pygame.draw.rect(screen, shadow_color, (x + shadow_thickness, y + height, width, shadow_thickness))
    pygame.draw.rect(screen, shadow_color, (x + width, y + shadow_thickness, shadow_thickness, height))

    # Draw box background
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, base_color, rect)

    # Draw border
    pygame.draw.rect(screen, border_color, rect, 2)

    # Padding inside box
    padding_x = 10
    padding_y = 5

    # Draw message text lines
    line1_surf = FONT.render(message, True, (31, 26, 22))

    max_width = width - padding_x
    filepath_to_show = filepath
    while small_font.size(filepath_to_show)[0] > max_width and len(filepath_to_show) > 3:
        filepath_to_show = filepath_to_show[:-4] + "..."

    line2_surf = small_font.render(filepath_to_show, True, (31, 26, 22))

    screen.blit(line1_surf, (x + padding_x, y + padding_y))
    screen.blit(line2_surf, (x + padding_x, y + padding_y + line1_surf.get_height() + 3))

class Button:
    def __init__(self, rect, text, font=FONT, padding=20):
        self.font = font
        self.text = text
        self.padding = padding

        # Measure text and adjust width
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        self.text_width = text_surf.get_width()
        self.text_height = text_surf.get_height()

        width = max(rect[2], self.text_width + self.padding * 2)
        height = max(rect[3], self.text_height + self.padding)

        self.rect = pygame.Rect(rect[0], rect[1], width, height)

        self.base_color = (255, 237, 212)
        self.border_color = (110, 67, 28)
        self.shadow_color = (110, 67, 28)
        self.hover_color = (231, 144, 50)
        self.active_color = (230, 101, 43)
        self.current_color = self.base_color

        self.is_hovered = False
        self.is_pressed = False
        self.is_active = False

    def update(self, mouse_pos, mouse_click):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.is_pressed = self.is_hovered and mouse_click

    def draw(self, surface):

        if self.is_pressed or self.is_active:
            self.current_color = self.active_color
        elif self.is_hovered:
            self.current_color = self.hover_color
        else:
            self.current_color = self.base_color

        x, y, w, h = self.rect
        shadow_thickness = 5

        # Shadows
        pygame.draw.rect(surface, self.shadow_color, (x + shadow_thickness, y + h, w, shadow_thickness))
        pygame.draw.rect(surface, self.shadow_color, (x + w, y + shadow_thickness, shadow_thickness, h))

        # Fill
        pygame.draw.rect(surface, self.current_color, self.rect)

        # Border
        pygame.draw.rect(surface, self.border_color, self.rect, 2)

        # Text
        label = self.font.render(self.text, True, (31, 26, 22))
        surface.blit(label, (
            x + (w - label.get_width()) // 2,
            y + (h - label.get_height()) // 2
        ))

    def was_clicked(self):
        return self.is_pressed


def draw_start_screen(mouse_pos, mouse_clicked, surprise_active):
    screen.blit(start_bg, (0, 0))
    draw_start_block(screen, (WIDTH, HEIGHT))

    # Container box margins
    box_x, box_y = int(WIDTH * 0.1), int(HEIGHT * 0.1)
    box_w, box_h = WIDTH - 2 * box_x, HEIGHT - 2 * box_y

    elements = []

    # Intro Text
    line1 = "Welcome to Shapey!"
    line2 = "Get creative and generate backgrounds with Python."

    screen.blit(FONT.render(line1, True, TEXT_COLOR), (box_x + 20, box_y + 20))
    screen.blit(FONT.render(line2, True, TEXT_COLOR), (box_x + 20, box_y + 50))

    # Vibe Buttons
    draw_text("Choose a vibe:", box_x + 20, box_y + 100)
    vibe_buttons = []
    vibe_start_x = box_x + 20
    vibe_start_y = box_y + 140
    gap = 20
    buttons_per_row = 4

    for i, vibe in enumerate(vibes):
        row = i // buttons_per_row
        col = i % buttons_per_row
        btn_rect = (vibe_start_x + col * 180, vibe_start_y + row * 70, 160, 40)
        btn = Button(btn_rect, vibe)
        btn.update(mouse_pos, mouse_clicked)
        vibe_buttons.append(btn)

    # "Surprise me" button
    random_btn_y = vibe_start_y + ((len(vibes) - 1) // buttons_per_row + 1) * 70 + 20
    btn_random = Button((vibe_start_x, random_btn_y, 180, 40), "Surprise me")

    btn_random.update(mouse_pos, mouse_clicked)
    btn_random.draw(screen)

    for i, btn in enumerate(vibe_buttons):
        btn.is_active = False if surprise_active else (i == selected_vibe_index)
        btn.draw(screen)

    btn_random.is_active = surprise_active

    # Complexity Slider
    slider_y = box_y + 400
    draw_text("Choose complexity:", box_x + 20, slider_y)
    slider_bar = pygame.Rect(box_x + 20, slider_y + 60, 200, 6)
    pygame.draw.rect(screen, (230, 101, 43), slider_bar)
    knob_x = box_x + 20 + ((complexity - 1) / 4) * 200
    knob_rect = pygame.Rect(knob_x - 10, slider_y + 53, 20, 20)
    pygame.draw.circle(screen, (110, 67, 28), knob_rect.center, knob_rect.width // 2)
    draw_text(f"{complexity}", box_x + 234, slider_y + 45)

    # Generate Button
    btn_generate = Button((box_x + 300, slider_y + 150, 180, 40), "Generate")
    btn_generate.draw(screen)

    return vibe_buttons, slider_bar, knob_rect, btn_generate, btn_random



def draw_display_screen():
    global generated_surface

    screen.blit(display_bg, (0, 0))

    if generated_surface:
        img_rect = generated_surface.get_rect(topleft=(59,47))
        screen.blit(generated_surface, img_rect)



def main_loop():
    global current_state, selected_vibe_index, complexity, generated_image, generated_surface
    global dropdown_open, dragging_slider
    global save_message, save_message_timer
    global surprise_active

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True
                if knob_rect.collidepoint(mouse_pos):
                    dragging_slider = True

            elif event.type == pygame.KEYDOWN:
                if current_state == STATE_START:
                    if event.key == pygame.K_RIGHT:
                        selected_vibe_index = (selected_vibe_index + 1) % len(vibes)
                    elif event.key == pygame.K_LEFT:
                        selected_vibe_index = (selected_vibe_index - 1) % len(vibes)
                    elif event.key == pygame.K_UP:
                        complexity = min(5, complexity + 1)
                    elif event.key == pygame.K_DOWN:
                        complexity = max(1, complexity - 1)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging_slider = False

        if dragging_slider:
            slider_left = slider_bar.left
            slider_right = slider_bar.right
            clamped_x = max(slider_left, min(mouse_pos[0], slider_right))

            percent = (clamped_x - slider_left) / (slider_right - slider_left)

            complexity = int(round(1 + percent * 4))

        if current_state == STATE_START:
            vibe_buttons, slider_bar, knob_rect, btn_generate, btn_random = draw_start_screen(mouse_pos, mouse_clicked, surprise_active)

            # Update all buttons
            for btn in vibe_buttons:
                btn.update(mouse_pos, mouse_clicked)

            btn_generate.update(mouse_pos, mouse_clicked)
            btn_random.update(mouse_pos, mouse_clicked)
            btn_generate.draw(screen)
            btn_random.draw(screen)

            # Handle clicks
            if mouse_clicked:
                for index, btn in enumerate(vibe_buttons):
                    if btn.rect.collidepoint(mouse_pos):
                        selected_vibe_index = index
                        surprise_active = False

                if btn_random.rect.collidepoint(mouse_pos):
                    selected_vibe_index = random.randint(0, len(vibes) - 1)
                    surprise_active = True

                if knob_rect.collidepoint(mouse_pos):
                    dragging_slider = True

                if btn_generate.was_clicked():
                    vibe = vibes[selected_vibe_index]
                    generated_image = generate_artwork(vibe, complexity)
                    generated_surface = pil_to_surface(generated_image)
                    current_state = STATE_DISPLAY



        elif current_state == STATE_DISPLAY:
            draw_display_screen()

            btn_save = Button(pygame.Rect(130, HEIGHT - 150, 200, 50), "Save Image")
            btn_new = Button(pygame.Rect(380, HEIGHT - 150, 200, 50), "Create New")
            btn_back = Button(pygame.Rect(630, HEIGHT - 150, 200, 50), "Back to Start")

            for btn in [btn_save, btn_new, btn_back]:
                btn.update(mouse_pos, mouse_clicked)
                btn.draw(screen)

            if save_message and pygame.time.get_ticks() - save_message_timer < 4000:
                box_width = 600
                box_height = 80
                box_x = (WIDTH - box_width) // 2
                box_y = HEIGHT - 300  # place it above the buttons (which are at HEIGHT-100)

                draw_message_box("Image saved to:", save_message, box_x, box_y, box_width, box_height)

            if mouse_clicked:

                if btn_save.was_clicked():
                    file_path = ask_save_path_safe()
                    if file_path:
                        pygame.image.save(generated_surface, file_path)
                        save_message = f"{file_path}"
                        save_message_timer = pygame.time.get_ticks()

                elif btn_new.was_clicked():

                    vibe = vibes[selected_vibe_index]
                    generated_image = generate_artwork(vibe, complexity)
                    generated_surface = pil_to_surface(generated_image)


                elif btn_back.was_clicked():
                    current_state = STATE_START

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main_loop()