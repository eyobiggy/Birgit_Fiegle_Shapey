import pygame
import random
import sys
from main import generate_artwork
from io import BytesIO
from PIL import Image

pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont("arial", 24)
BG_COLOR = (240, 240, 240)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapey")

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

import os
import time

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
    label = FONT.render(text, True, BLACK)
    screen.blit(label, (x, y))


def draw_button(label, rect, color=(180, 180, 180)):
    pygame.draw.rect(screen, color, rect)
    draw_text(label, rect.x + 10, rect.y + 10)
    return rect


def draw_start_screen():
    screen.fill(BG_COLOR)

    # --- Vibe Buttons ---
    draw_text("Choose a vibe:", 50, 40)
    vibe_buttons = []
    start_x = 50
    for i, vibe in enumerate(vibes):
        btn_rect = pygame.Rect(start_x, 70, 100, 40)
        color = (150, 200, 255) if i == selected_vibe_index else (200, 200, 200)
        pygame.draw.rect(screen, color, btn_rect)
        draw_text(vibe, btn_rect.x + 5, btn_rect.y + 10)
        vibe_buttons.append((btn_rect, i))
        start_x += 110  # spacing

    # --- Slider for complexity ---
    draw_text("Choose complexity:", 50, 250)
    slider_bar = pygame.Rect(50, 280, 200, 6)
    pygame.draw.rect(screen, (180, 180, 180), slider_bar)
    knob_x = 50 + ((complexity - 1) / 4) * 200
    knob_rect = pygame.Rect(knob_x - 10, 275, 20, 20)
    pygame.draw.rect(screen, (100, 100, 255), knob_rect)
    draw_text(f"{complexity}", 270, 270)

    # --- Generate button ---
    btn_generate = draw_button("Generate", pygame.Rect(50, 340, 150, 40))

    return vibe_buttons, slider_bar, knob_rect, btn_generate


def draw_display_screen():
    screen.fill(BG_COLOR)
    global generated_surface

    # Draw the generated image
    if generated_surface:
        img_rect = generated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(generated_surface, img_rect)

    # Draw buttons
    btn_save = draw_button("Save Image", pygame.Rect(100, HEIGHT - 100, 150, 40))
    btn_new = draw_button("Create New", pygame.Rect(300, HEIGHT - 100, 150, 40))
    btn_back = draw_button("Back to Start", pygame.Rect(500, HEIGHT - 100, 150, 40))
    return btn_save, btn_new, btn_back


def main_loop():
    global current_state, selected_vibe_index, complexity, generated_image, generated_surface
    global dropdown_open, dragging_slider
    global save_message, save_message_timer

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

        if current_state == STATE_START:
            vibe_buttons, slider_bar, knob_rect, btn_generate = draw_start_screen()

            if mouse_clicked:
                # Check vibe button clicks
                for rect, index in vibe_buttons:
                    if rect.collidepoint(mouse_pos):
                        selected_vibe_index = index
                        break

                # Clicked slider knob to drag
                if knob_rect.collidepoint(mouse_pos):
                    dragging_slider = True

                # Clicked generate button
                elif btn_generate.collidepoint(mouse_pos):
                    vibe = vibes[selected_vibe_index]
                    generated_image = generate_artwork(vibe, complexity)
                    generated_surface = pil_to_surface(generated_image)
                    current_state = STATE_DISPLAY
                    dropdown_open = False  # close dropdown after generate

            # Slider dragging
            if dragging_slider:
                slider_x = max(50, min(mouse_pos[0], 250))  # clamp within slider range
                percent = (slider_x - 50) / 200
                complexity = int(percent * 4) + 1  # maps slider to 1–5

        elif current_state == STATE_DISPLAY:
            btn_save, btn_new, btn_back = draw_display_screen()

            if save_message and pygame.time.get_ticks() - save_message_timer < 3000:
                draw_text(save_message, 50, HEIGHT - 50)

            if mouse_clicked:
                if btn_save.collidepoint(mouse_pos):
                    file_path = ask_save_path_safe()
                    if file_path:
                        pygame.image.save(generated_surface, file_path)
                        save_message = f"Image saved to: {file_path}"
                        save_message_timer = pygame.time.get_ticks()

                elif btn_new.collidepoint(mouse_pos):
                    vibe = vibes[selected_vibe_index]
                    generated_image = generate_artwork(vibe, complexity)
                    generated_surface = pil_to_surface(generated_image)
                elif btn_back.collidepoint(mouse_pos):
                    current_state = STATE_START

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main_loop()