import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def string_to_binary(text):
    """Chuyển chuỗi thành nhị phân."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_string(binary_text):
    """Chuyển nhị phân thành chuỗi."""
    chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)

def hide_message():
    """Ẩn tin nhắn vào ảnh."""
    text = entry_message.get()
    if not text or not image_path:
        messagebox.showerror("Lỗi", "Vui lòng chọn ảnh và nhập tin nhắn!")
        return
    
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    pixels = img.load()
    
    binary_text = string_to_binary(text) + '1111111111111110'
    data_index, binary_length = 0, len(binary_text)

    for y in range(height):
        for x in range(width):
            if data_index < binary_length:
                r, g, b = pixels[x, y]
                r = (r & 0b11111110) | int(binary_text[data_index])  
                data_index += 1
                if data_index < binary_length:
                    g = (g & 0b11111110) | int(binary_text[data_index])  
                    data_index += 1
                if data_index < binary_length:
                    b = (b & 0b11111110) | int(binary_text[data_index])  
                    data_index += 1
                pixels[x, y] = (r, g, b)

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Thành công", f"Ảnh đã lưu: {save_path}")

def extract_message():
    """Trích xuất tin nhắn từ ảnh."""
    global image_path
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    binary_text = ""

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_text += str(r & 1) + str(g & 1) + str(b & 1)
            if "1111111111111110" in binary_text:
                binary_text = binary_text[:binary_text.index("1111111111111110")]
                break
        break

    messagebox.showinfo("Tin nhắn", f"🔍 Tin nhắn trích xuất: {binary_to_string(binary_text)}")

def open_image():
    """Chọn ảnh từ máy tính."""
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        img = Image.open(image_path)
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        label_img.config(image=img_tk)
        label_img.image = img_tk

# --------- Giao diện Tkinter ---------
root = tk.Tk()
root.title("Steganography - LSB")

image_path = ""

frame = tk.Frame(root)
frame.pack(pady=10)

label_img = tk.Label(frame)
label_img.pack()

btn_open = tk.Button(root, text="📂 Chọn ảnh", command=open_image)
btn_open.pack(pady=5)

entry_message = tk.Entry(root, width=50)
entry_message.pack(pady=5)
entry_message.insert(0, "Nhập tin nhắn...")

btn_hide = tk.Button(root, text="📝 Ẩn tin nhắn", command=hide_message)
btn_hide.pack(pady=5)

btn_extract = tk.Button(root, text="🔍 Trích xuất tin nhắn", command=extract_message)
btn_extract.pack(pady=5)

root.mainloop()
