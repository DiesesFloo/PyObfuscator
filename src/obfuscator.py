import customtkinter
from customtkinter import *
import tkinter.messagebox
import os
import subprocess


class Obfuscator:
    def __init__(self):
        self.root = customtkinter.CTk()
        self._filepath = ""

        self.root.geometry("800x550")
        self.root.title("Python Obfuscator")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.file_path_label = customtkinter.CTkLabel(master=self.frame, text="Select the file you wanna obfuscate")
        self.select_file_button = customtkinter.CTkButton(master=self.frame, text="Select File",
                                                          command=self.on_select_file_button_submit)
        self.obfuscate_button = customtkinter.CTkButton(master=self.frame, text="Obfuscate",
                                                        command=self.on_obfuscate_button_submit, state="disabled")

        self.construct_main_window()

        self.root.mainloop()

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, new_filepath):
        self._filepath = new_filepath

        if self.filepath == "":
            self.file_path_label.configure(text="Select the file you wanna obfuscate")
            self.obfuscate_button.configure(state="disabled")
            return

        self.file_path_label.configure(text=f"Selected file: {self.filepath}")
        self.obfuscate_button.configure(state="normal")

    def construct_main_window(self):
        self.file_path_label.pack(pady=(200, 10))
        self.select_file_button.pack(pady=10)
        self.obfuscate_button.pack(pady=10)

    def destroy_main_window(self):
        self.file_path_label.destroy()
        self.select_file_button.destroy()
        self.obfuscate_button.destroy()

    def on_select_file_button_submit(self):
        filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])

        if filepath == "":
            return

        self.filepath = filepath

    def on_obfuscate_button_submit(self):

        directory = os.path.dirname(self.filepath)
        name = os.path.basename(self.filepath)

        subprocess.call(["pyarmor", "obfuscate", "--output=%s/obfuscated" % directory, self.filepath],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

        self.filepath = ""

        tkinter.messagebox.showinfo("Python Obfuscator", f"The obfuscate of {name} was successful!")

        return


if __name__ == "__main__":
    obfuscator = Obfuscator()
