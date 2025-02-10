import cv2
import numpy as np
import matplotlib.pyplot as plt

def lsb_steganalysis(image_path):
    """Trích xuất mặt phẳng bit LSB của ảnh."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    lsb_plane = img & 1  # Lấy bit ít quan trọng nhất
    return lsb_plane

# Đọc hai ảnh
original_lsb = lsb_steganalysis("conkhingu.jpg")
stego_lsb = lsb_steganalysis("output.png")

# Hiển thị hai ảnh cạnh nhau để so sánh
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_lsb, cmap='gray')
plt.title("LSB Plane - Original")

plt.subplot(1, 2, 2)
plt.imshow(stego_lsb, cmap='gray')
plt.title("LSB Plane - Stego Image")

plt.show()


