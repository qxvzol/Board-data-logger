import tkinter as tk
root = tk.Tk()
root.geometry("400x400")
root.title("Variables")

text_var1= tk.StringVar()
text_var1.set("Hello, World!")
label1 = tk.Label(root, 
textvariable=text_var1)

def UI(var1):
    a=("var1: ",str(var1))
    text_var1.set(a)

    label1.pack()
    root.update()