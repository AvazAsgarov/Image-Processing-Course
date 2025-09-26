from PIL import Image

# Task 1: Read and Display an Image
img = Image.open('solo_turk.jpeg')
img.show()

# Task 2: Print Details about the Image
print(f"Format of the Image: {img.format}")   # Format
print(f"Mode of the Image: {img.mode}")       # Mode
print(f"Size of the Image: {img.size}")       # Size

# Task 3: Change the Image Type (JPEG -> PNG)
img.save("solo_turk.png")

# Task 4: Resize the Image
resized = img.resize((200, 200))
resized.show()
resized.save("solo_turk_resized.png")

# Task 5: Crop the Image
cropped = img.crop((100, 200, 300, 400))  # (left, upper, right, lower)
cropped.show()
cropped.save("solo_turk_cropped.png")

# Task 6: Rotate the Image
rotated = img.rotate(45, expand=True)
rotated.show()
rotated.save("solo_turk_rotated.png")

# Task 7: Mirror the Image (left <-> right)
mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrored.show()
mirrored.save("solo_turk_mirrored.png")

# Task 8: Flip the Image (top <-> bottom)
flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
flipped.show()
flipped.save("solo_turk_flipped.png")