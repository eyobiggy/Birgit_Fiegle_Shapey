import random
import colorsys
from colorsys import hsv_to_rgb

class Palette:
    def __init__(self, base_hue_range=(0,360), saturation_range=(0.0,1.0), value_range=(0.0,1.0)):
        self.base_hue_range = base_hue_range
        self.saturation_range = saturation_range
        self.value_range = value_range

    def generate(self, n=6):
        palette = []
        base_hue = random.randint(*self.base_hue_range)

        for _ in range(n):
            hue = (base_hue + random.randint(-20,20)) % 360
            sat = random.uniform(*self.saturation_range)
            val = random.uniform(*self.value_range)
            rgb = hsv_to_rgb(hue/360, sat, val)
            rgb_255 = tuple(int(x*255) for x in rgb)
            palette.append('#{:02x}{:02x}{:02x}'.format(*rgb_255))

        return palette

    ## add def contrast_colour later?


class ColourfulPalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(0,360), saturation_range=(0.8,1.0), value_range=(0.9,1.0))

class SunshinePalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(20,60), saturation_range=(0.9,1.0), value_range=(0.7,1.0))

class DarkPalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(0,360), saturation_range=(0.0,1.0), value_range=(0.0,0.15))

class PastelPalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(0,360), saturation_range=(0.0,0.4), value_range=(0.9,1.0))

class OceanPalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(160,250), saturation_range=(0.0,1.0), value_range=(0.7,1.0))

class BeigePalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(30,40), saturation_range=(0.1,0.5), value_range=(0.5,1.0))

class ForestPalette(Palette):
    def __init__(self):
        super().__init__(base_hue_range=(80,130), saturation_range=(0.5,0.9), value_range=(0.1,0.5))


