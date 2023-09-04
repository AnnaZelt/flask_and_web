import tkinter as tk

# def change_color(button,new,name):
#     button.config(text=name, bg=new)

# root.title("Color buttons")
# label = tk.Label(root, text="Hello, Tkinter!")
# b1=tk.Button(root, text='Red', width=25, command=lambda: change_color(b1,"red","Red"))
# b2=tk.Button(root, text='Blue', width=25, command=lambda: change_color(b2,"blue","Blue"))
# b3=tk.Button(root, text='Green', width=25, command=lambda: change_color(b3,"green","Green"))
# label.pack()
# b1.pack()
# b2.pack()
# b3.pack()
# b1=tk.Button(root, text='save', width=25, command=lambda)
# b2=tk.Button(root, text='load', width=25, command=lambda)

# FILE_PATH = "notepad.txt"

# def save_file():
#     with open(FILE_PATH, "w") as file:
#         file.write(text_widget.get("1.0", "end"))

# def load_file():
#     try:
#         with open(FILE_PATH, "r") as file:
#             text_widget.delete("1.0", "end")
#             text_widget.insert("1.0", file.read())
#     except FileNotFoundError:
#         print("File not found.")
#         return

# root = tk.Tk()
# root.title("Notepad")

# text_widget = tk.Text(root)
# text_widget.pack()

# menu_bar = tk.Menu(root)
# root.config(menu=menu_bar)

# file_menu = tk.Menu(menu_bar, tearoff=False)
# menu_bar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_command(label="Open", command=load_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# # Load the file content when the application starts
# load_file()

from tkinter import PhotoImage

root = tk.Tk()
root.title("Images")

def show_image(new_image):
    label.config(image=new_image, width=500,height=400)
    label.image = new_image

img1 = PhotoImage(file=".\images\img1.png")
img2 = PhotoImage(file='.\images\img2.png')
b1=tk.Button(root, text='Image 1', width=25, command=lambda: show_image(img1))
b2=tk.Button(root, text='Image 2', width=25, command=lambda: show_image(img2))

label = tk.Label(root, image=img1)
label.pack()
b1.pack()
b2.pack()
root.mainloop()

