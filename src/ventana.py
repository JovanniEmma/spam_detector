import tkinter as tk 
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("avisop","boton presionado")

ventana = tk.Tk()
ventana.title("ventana simple")
ventana.geometry("400x300")
label = tk.Label(ventana, text="Hola mundo")
label.pack()


def on_button_click():
    label.config(text="t amo sizu")

button = tk.Button(ventana, text="Click Me", command=on_button_click)
button.pack()

button = tk.Button(ventana, text="sizu Me", command=mostrar_mensaje)
button.pack(pady=20)

ventana.mainloop()