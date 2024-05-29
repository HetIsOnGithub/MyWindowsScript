import os
from tkinter import Tk, Label, Button, Entry, filedialog, IntVar, Scale
from PIL import Image

class ImageCompressorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Compressor")

        self.label = Label(master, text="Select an image to compress")
        self.label.pack()

        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.quality_label = Label(master, text="Select compression quality (1-100):")
        self.quality_label.pack()

        self.quality = IntVar(value=85)
        self.quality_scale = Scale(master, from_=1, to=100, orient="horizontal", variable=self.quality)
        self.quality_scale.pack()

        self.compress_button = Button(master, text="Compress Image", command=self.compress_image)
        self.compress_button.pack()

        self.output_label = Label(master, text="")
        self.output_label.pack()

        self.input_file = ""
        self.output_file = ""

    def select_image(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if self.input_file:
            self.label.config(text=f"Selected image: {self.input_file}")

    def compress_image(self):
        if not self.input_file:
            self.output_label.config(text="Please select an image first.")
            return
        
        self.output_file = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg;*.jpeg")])
        if not self.output_file:
            return

        quality = self.quality.get()
        try:
            with Image.open(self.input_file) as img:
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(self.output_file, "JPEG", quality=quality)
                self.output_label.config(text=f"Image compressed and saved to {self.output_file}")
        except Exception as e:
            self.output_label.config(text=f"An error occurred: {e}")

def main():
    root = Tk()
    app = ImageCompressorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
