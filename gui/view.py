import tkinter
import os
from tkinter import *
from pathlib import Path

from convertor_engine.docxtopdf import fun as convert
from convertor_engine.docxtopdf import printer
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

SCRIPT_DIR = Path(__file__).parent
test_file = SCRIPT_DIR / "test.docx"  # Now looks in the same folder as view.py
output_folder = SCRIPT_DIR.parent / "generated_pdfs"  # Goes up one level
printer()
print(f"Current directory: {os.getcwd()}")
print(f"Script directory: {SCRIPT_DIR}")
print(f"Test file exists: {test_file.exists()}")
print(f"Test file full path: {test_file.absolute()}")
print(f"Output folder: {output_folder.absolute()}")

# Create output folder if it doesn't exist
output_folder.mkdir(exist_ok=True)

# Run conversion
convert(str(test_file), str(output_folder))

# checking if tkinter is installed with its version
# print(tkinter.TkVersion)

# browsing in tkinter
# def browse_files():
#     filename = filedialog.askopenfilename(
#         initialdir = "/",
#         title = "Select a File",
#         filetypes = (("Word Documents", "*.docx"),
#             ("PDF Files", "*.pdf"),
#             ("Text Files", "*.txt"),
#           https://chatgpt.com/c/68010ead-a668-8010-8f46-b8b0a433b2eb  ("All Files", "*.*"))
#     )
#     label_file_explorer.configure(text="File Opened: " + filename)

# # function for saving files
# def save_file():
#     file = asksaveasfile(
#         filetypes = (
#             ("PDF Files", "*.pdf"),
#             ("Text Files", "*.txt"),
#             ("All Files", "*.*")),
#         defaultextension = "*.pdf"  # Specify default extension here
#     )
#     if file:
#         # If the user selects a file, print the file path
#         print("File saved as:", file.name)


# # root window
# window = Tk()

# # setting the window title
# window.title('File Selector')

# # Setting window size
# window.geometry("500x500")

# #Set window background color
# window.config(background = "white")

# # Create a File Explorer label
# label_file_explorer = Label(window,
#     text = "File Explorer using Tkinter",
#     width = 100, height = 4,
#     fg = "blue")


# button_explore = Button(window,
#     text = "Browse Files",
#     command = browse_files)

# # button for exit
# button_exit = Button(window,
#     text = "Exit",
#     command = window.quit)

# # button for saving the file
# button_save = Button(
#     window,
#     text = "Save file",
#     command = save_file
# )

# # button for converting the file
# # button_convert = Button(
# #     window,
# #     text = "Convert to pdf",
# #     command = convert
# # )


# # # Grid method is chosen for placing
# # # the widgets at respective positions
# # # in a table like structure by
# # # specifying rows and columns
# label_file_explorer.grid(column = 1, row = 1)

# button_explore.grid(column = 1, row = 2)

# button_save.grid(column = 1, row = 3)

# button_exit.grid(column = 1,row = 4)

# # Let the window wait for any events
# # mainloop?
# window.mainloop()


# drag and dropping the file

# test_file = "./test.docx"
# output_folder = "../generated_pdfs"
# print(f"Current directory: {os.getcwd()}")
# print(f"Test file exists: {os.path.exists(test_file)}")
# print(f"Output folder: {os.path.abspath(output_folder)}")
# convert(test_file, output_folder)

# print("hi from view.py")
