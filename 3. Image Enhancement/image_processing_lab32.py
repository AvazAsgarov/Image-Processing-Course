import cv2 as cv
import matplotlib.pyplot as plt

# Read images
ronaldo_img = cv.imread("ronaldo.png")
messi_img = cv.imread("messi.png")

# Resize images to the same size
target_size = (1200, 740)
ronaldo_resized = cv.resize(ronaldo_img, target_size)
messi_resized = cv.resize(messi_img, target_size)

# Convert BGR to RGB for Matplotlib
ronaldo_rgb = cv.cvtColor(ronaldo_resized, cv.COLOR_BGR2RGB)
messi_rgb = cv.cvtColor(messi_resized, cv.COLOR_BGR2RGB)

# Addition
added_img = cv.add(ronaldo_resized, messi_resized)
cv.imwrite("ronaldo_messi_addition.png", added_img)
added_rgb = cv.cvtColor(added_img, cv.COLOR_BGR2RGB)

# Subtraction
subtracted_img = cv.subtract(ronaldo_resized, messi_resized)
cv.imwrite("ronaldo_messi_subtraction.png", subtracted_img)
subtracted_rgb = cv.cvtColor(subtracted_img, cv.COLOR_BGR2RGB)

# Multiplication with scalar
scalar_mult = 1.5
multiplied_img = cv.convertScaleAbs(ronaldo_resized * scalar_mult)
cv.imwrite("ronaldo_multiplication.png", multiplied_img)
multiplied_rgb = cv.cvtColor(multiplied_img, cv.COLOR_BGR2RGB)

# Division with scalar
scalar_div = 2.0
divided_img = cv.convertScaleAbs(ronaldo_resized / scalar_div)
cv.imwrite("ronaldo_division.png", divided_img)
divided_rgb = cv.cvtColor(divided_img, cv.COLOR_BGR2RGB)

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

axes[0, 0].imshow(ronaldo_rgb)
axes[0, 0].set_title("Ronaldo")
axes[0, 0].axis("off")

axes[0, 1].imshow(messi_rgb)
axes[0, 1].set_title("Messi")
axes[0, 1].axis("off")

axes[0, 2].imshow(added_rgb)
axes[0, 2].set_title("Addition")
axes[0, 2].axis("off")

axes[1, 0].imshow(subtracted_rgb)
axes[1, 0].set_title("Subtraction")
axes[1, 0].axis("off")

axes[1, 1].imshow(multiplied_rgb)
axes[1, 1].set_title(f"Multiplication x{scalar_mult}")
axes[1, 1].axis("off")

axes[1, 2].imshow(divided_rgb)
axes[1, 2].set_title(f"Division ÷{scalar_div}")
axes[1, 2].axis("off")

plt.tight_layout()
plt.show()