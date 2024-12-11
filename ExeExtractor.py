import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pyunpack import Archive

class ExeExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("ExeExtractor - EXE Unpacker")
        self.root.geometry("400x200")

        # Input file label and button
        self.file_label = tk.Label(root, text="Select an EXE File:")
        self.file_label.pack(pady=5)

        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.pack(pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        # Output directory label and button
        self.output_label = tk.Label(root, text="Select Output Directory:")
        self.output_label.pack(pady=5)

        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.pack(pady=5)

        self.output_button = tk.Button(root, text="Browse", command=self.browse_output_directory)
        self.output_button.pack(pady=5)

        # Unpack button
        self.unpack_button = tk.Button(root, text="Unpack EXE", command=self.unpack_exe)
        self.unpack_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def browse_output_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory)

    def unpack_exe(self):
        exe_file = self.file_entry.get()
        output_dir = self.output_entry.get()

        if not exe_file or not output_dir:
            messagebox.showerror("Error", "Please select both an EXE file and an output directory.")
            return

        if not os.path.isfile(exe_file):
            messagebox.showerror("Error", "The selected EXE file does not exist.")
            return

        if not os.path.isdir(output_dir):
            messagebox.showerror("Error", "The selected output directory does not exist.")
            return

        try:
            Archive(exe_file).extractall(output_dir)
            messagebox.showinfo("Success", f"EXE file unpacked successfully to {output_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to unpack the EXE file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExeExtractor(root)
    root.mainloop()
