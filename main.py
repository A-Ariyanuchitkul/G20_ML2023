import tkinter as tk
from tkinter import filedialog
import nibabel as nib
import numpy as np
from PIL import Image, ImageTk

#from project_classification import *

# Import your machine learning model
# Replace the following line with your actual model import
# from your_ml_module import your_ml_model_function
def your_ml_model_function(input_data):
     generated_image = None     # Your model logic here
     return generated_image

class FMRIModelGUI:
    def __init__(self, master):
        self.master = master
        master.title("fMRI Model GUI")

        self.input_file_label = tk.Label(master, text="Select fMRI Data File:")
        self.input_file_label.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.predict_button = tk.Button(master, text="Generate Image", command=self.generate_image)
        self.predict_button.pack()

        self.result_image_label = tk.Label(master, text="Generated Image:")
        self.result_image_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("NIfTI files", "*.nii;*.nii.gz")])
        self.input_file_label.config(text=f"Selected File: {file_path}")
        self.fMRI_data = nib.load(file_path).get_fdata()

    def generate_image(self):
        if not hasattr(self, 'fMRI_data'):
            tk.messagebox.showerror("Error", "Please select an fMRI data file first.");
            return;
        generated_image = your_ml_model_function(self.fMRI_data);
        self.display_image(generated_image);

    def display_image(self, img_array):                                         #CHANGE TO MATPLOTLIB LATER
        img_array = np.uint8(img_array * 255)  # Convert to 8-bit for display
        img = Image.fromarray(img_array)
        img = img.resize((300, 300))  # Adjust the size as needed

        img_tk = ImageTk.PhotoImage(img)

        if hasattr(self, 'result_label'):
            self.result_label.configure(image=img_tk)
            self.result_label.image = img_tk
        else:
            self.result_label = tk.Label(self.master, image=img_tk)
            self.result_label.pack()

# Create the main GUI window
root = tk.Tk()
app = FMRIModelGUI(root)
root.mainloop()
