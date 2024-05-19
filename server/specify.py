import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from util import classify_image

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            self.display_image(image)
            self.process_image(file_path)

    def display_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def process_image(self, file_path):
        try:
            with open(file_path, "rb") as f:
                image_base64_data = f.read()
                result = classify_image(image_base64_data, file_path)
                self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_result(self, result):
        if result:
            self.result_label.config(text=f"Result: {result}")
        else:
            self.result_label.config(text="No faces found or recognition failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
