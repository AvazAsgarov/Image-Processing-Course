import cv2 as cv

# Task 1: Read and Display the Original Image
img = cv.imread("ronaldo.jpg")
cv.imshow("Original Image", img)

# Task 2: Print Details about the Image
print(f"Image Shape (H x W x C): {img.shape}")
print(f"Total Number of Pixels: {img.size}")

# Task 3: Convert the Image to Grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", img_gray)
cv.imwrite("ronaldo_grayscale.png", img_gray)

# Task 4: Find Color of Pixel at [70, 100]
pixel_color = img[70, 100]
print(f"Color of Pixel at [70, 100]: {pixel_color}")  # BGR format

# Task 5: Modify the Pixel Value at [200, 150] to Red
img_modified = img.copy()
img_modified[200, 150] = [0, 0, 255]  # Red in BGR
cv.imshow("Red Pixel Modified", img_modified)
cv.imwrite("ronaldo_red_pixel.png", img_modified)

# Task 6: Modify a Region to Green [100:300, 150:400]
img_modified[100:300, 150:400] = [0, 255, 0]  # Green in BGR
cv.imshow("Green Region Modified", img_modified)
cv.imwrite("ronaldo_green_region.png", img_modified)

# Task 7: Resize the Image
img_smaller = cv.resize(img_modified, (400, 400))
img_larger = cv.resize(img_modified, (1000, 1000))

cv.imshow("Resized Smaller Image", img_smaller)
cv.imshow("Resized Larger Image", img_larger)

cv.imwrite("ronaldo_smaller.png", img_smaller)
cv.imwrite("ronaldo_larger.png", img_larger)

# Task 8: Rotate the Image
img_rotate_180 = cv.rotate(img_modified, cv.ROTATE_180)
img_rotate_90_cw = cv.rotate(img_modified, cv.ROTATE_90_CLOCKWISE)
img_rotate_90_ccw = cv.rotate(img_modified, cv.ROTATE_90_COUNTERCLOCKWISE)

cv.imshow("Rotated 180°", img_rotate_180)
cv.imshow("Rotated 90° Clockwise", img_rotate_90_cw)
cv.imshow("Rotated 90° Counterclockwise", img_rotate_90_ccw)

cv.imwrite("ronaldo_rotated_180.png", img_rotate_180)
cv.imwrite("ronaldo_rotated_90_cw.png", img_rotate_90_cw)
cv.imwrite("ronaldo_rotated_90_ccw.png", img_rotate_90_ccw)

# Task 9: Flip Image Horizontally and Vertically
img_flip_vertical = cv.flip(img_modified, 0)
img_flip_horizontal = cv.flip(img_modified, 1)

cv.imshow("Flipped Vertically", img_flip_vertical)
cv.imshow("Flipped Horizontally", img_flip_horizontal)

cv.imwrite("ronaldo_flipped_vertical.png", img_flip_vertical)
cv.imwrite("ronaldo_flipped_horizontal.png", img_flip_horizontal)

cv.waitKey(0)
cv.destroyAllWindows()
