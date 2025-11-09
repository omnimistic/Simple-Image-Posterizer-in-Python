from PIL import Image, ImageEnhance
import numpy as np

source = input("what is the path to your image?: ")
color_limit = int(input("enter the no. of colors you want: "))
contrast = float(input("enter the amount of contrast you want, 1.5 is suggested: "))
output_path = input("what is the path to your output location?: ")

mode = int(input("enter 1 for default mode and 2 for custom color mode: "))

output_path = output_path + "\\output.png"

if mode == 2:
    print("\nEnter your custom tint color (RGB values 0-255):")
    r = int(input("Red (0-255): "))
    g = int(input("Green (0-255): "))
    b = int(input("Blue (0-255): "))

    custom_color = (r, g, b)


def create_custom_palette(base_color, num_colors):

    r, g, b = base_color
    palette = []
    
    
    for i in range(num_colors):
        if i < num_colors // 2:
            factor = i / (num_colors // 2)
            palette.append((
                int(r * factor),
                int(g * factor),
                int(b * factor)
            ))
        else:
            factor = (i - num_colors // 2) / (num_colors // 2)
            palette.append((
                int(r + (255 - r) * factor),
                int(g + (255 - g) * factor),
                int(b + (255 - b) * factor)
            ))
    
    return palette


def process_image(source, output_path, color_limit, contrast, tint_color):
    img = Image.open(source)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    palette = create_custom_palette(tint_color, color_limit)
    
    pixels = np.array(img)
    h, w = pixels.shape[:2]
    pixels_flat = pixels.reshape(-1, 3)

    result = np.zeros_like(pixels_flat)
    for i, pixel in enumerate(pixels_flat):
        distances = [np.sum((pixel - np.array(color))**2) for color in palette]
        closest = np.argmin(distances)
        result[i] = palette[closest]

    result = result.reshape(h, w, 3).astype(np.uint8)
    output_img = Image.fromarray(result)
    
    output_img.save(output_path)
    print(f"Saved to {output_path}")
    output_img.show()


def default_process_image(source, output_path, color_limit, contrast):
    img = Image.open(source)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    enhancer = ImageEnhance.Contrast(img)
    contrasted_img = enhancer.enhance(contrast)
    quantized_img = contrasted_img.quantize(colors=color_limit, dither=Image.Dither.FLOYDSTEINBERG)
    output_img = quantized_img.convert('RGB')
    output_img.save(output_path)
    print(f"Saved to {output_path}")

    output_img.show()

if mode == 1:
    default_process_image(source, output_path, color_limit, contrast)
elif mode == 2:
    process_image(source, output_path, color_limit, contrast, custom_color)
else:
    print("invalid mode")


