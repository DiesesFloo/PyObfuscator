import customtkinter
from customtkinter import *
import tkinter.messagebox
import os
import subprocess

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Python Obfuscator")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


def on_submit():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])

    if filepath == "":
        return

    directory = os.path.dirname(filepath)
    name = os.path.basename(filepath)
    subprocess.call(["pyarmor", "obfuscate", "--output=%s/obfuscated" % directory, filepath], stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL)
    tkinter.messagebox.showinfo("Python Obfuscator", f"The obfuscate of {name} was successful!")


label = customtkinter.CTkLabel(master=frame, text="Select the file you wanna obfuscate")
label.pack(pady=(100, 10))

button1 = customtkinter.CTkButton(master=frame, text="Obfuscate", command=on_submit)
button1.pack(pady=10)

root.mainloop()
