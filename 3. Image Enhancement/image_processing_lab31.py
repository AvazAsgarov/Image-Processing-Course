from PIL import Image, ImageEnhance

# Task 1: Read and Display the Original Image
original_image = Image.open("flame_towers.png")
original_image.show(title="Original Image")
original_image.save("flame_towers_original.png")

# Task 2: Increase Brightness
bright_image = ImageEnhance.Brightness(original_image).enhance(1.5)
bright_image.show(title="Brightness Increased")
bright_image.save("flame_towers_brightness.png")

# Task 3: Increase Contrast
contrast_image = ImageEnhance.Contrast(original_image).enhance(2.0)
contrast_image.show(title="Contrast Increased")
contrast_image.save("flame_towers_contrast.png")

# Task 4: Increase Sharpness
sharp_image = ImageEnhance.Sharpness(original_image).enhance(4.0)
sharp_image.show(title="Sharpness Increased")
sharp_image.save("flame_towers_sharpness.png")