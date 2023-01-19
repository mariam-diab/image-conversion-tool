import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
from image_processor import *

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CodeSmith")
        self.image_processor = image_processor()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Welcome to CodeSmith Image Convertor and Resizer!")
        self.title_label.grid(row=0, column=0, columnspan=5)
        self.select_image_button = tk.Button(self.root, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=1, column=0, columnspan=5)
        self.file_format_label = tk.Label(self.root, text="Select the Desired Format")
        self.file_format_label.grid(row=2, column=0, columnspan=5)
        self.file_format_dropdown = Combobox(self.root, values=list(image_adapter._adapters.keys()))
        self.file_format_dropdown.set("jpg")
        self.file_format_dropdown.grid(row=3, column=0, columnspan=5)
        self.width_label = tk.Label(self.root, text="Width: ")
        self.width_label.grid(row=4, column=0)
        self.width_entry = tk.Entry(self.root)
        self.width_entry.grid(row=4, column=1)
        self.width_entry.insert(0, "800")
        self.height_label = tk.Label(self.root, text="Height: ")
        self.height_label.grid(row=4, column=2)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=4, column=3)
        self.height_entry.insert(0, "600")
        self.save_button = tk.Button(self.root, text="Save", command=self.convert_resize_save)
        self.save_button.grid(row=5, column=0, columnspan=5)

    def select_image(self):
        file_path = filedialog.askopenfilename()
        try:
            self.image_processor.open_image(file_path)
            self.select_image_button.config(text="Selected!", bg="green")
        except ValueError as e:
            self.select_image_button.config(text="Invalid Format", bg="red")
            tk.messagebox.showerror("Error", e)

    def convert_resize_save(self):
        file_path = filedialog.asksaveasfilename()
        try:
            width = self.width_entry.get()
            height = self.height_entry.get()
            self.image_processor.save_image(file_path, width, height)
        except ValueError as e:
            tk.messagebox.showerror("Error", e)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()