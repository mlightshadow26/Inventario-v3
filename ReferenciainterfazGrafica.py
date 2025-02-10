import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.title("Control de inventario Py")

ventana_principal.geometry("600x400")
# Frames
frame_principal = tk.Frame(ventana_principal)
frame_2 = tk.Frame(ventana_principal)
frame_3 = tk.Frame(ventana_principal)
frame_4 = tk.Frame(ventana_principal)

# Etiquetas
label_titulo_1 = tk.Label(frame_principal, text="Contenido principal")
label_titulo_2 = tk.Label(frame_2, text="Contenido 2")
label_titulo_3 = tk.Label(frame_3, text="Contenido 3")
label_titulo_4 = tk.Label(frame_4, text="Contenido 4")

# Botones
boton_1 = tk.Button(frame_principal, text="Soy un botón", command=lambda: print("Hola"))
boton_2 = tk.Button(frame_principal, text="Soy un botón", command=lambda: print("Hola"))
boton_3 = tk.Button(frame_principal, text="Soy un botón", command=lambda: print("Hola"))
boton_4 = tk.Button(frame_principal, text="Soy un botón", command=lambda: print("Hola"))

boton_5 = tk.Button(frame_2, text="Soy un botón", command=lambda: print("Hola"))
boton_6 = tk.Button(frame_2, text="Soy un botón", command=lambda: print("Hola"))
boton_7 = tk.Button(frame_2, text="Soy un botón", command=lambda: print("Hola"))
boton_8 = tk.Button(frame_2, text="Soy un botón", command=lambda: print("Hola"))


# Campos


# Campos de texto



# Ejecución de los frames
frame_principal.grid(column=0, row=0)
frame_2.grid(column=1, row=0)
frame_3.grid(column=0, row=1)
frame_4.grid(column=1, row=1)

# Ejecución de los widgets
label_titulo_1.pack()
label_titulo_2.pack()
label_titulo_3.pack()
label_titulo_4.pack()

boton_1.pack()
boton_2.pack()
boton_3.pack()
boton_4.pack()
boton_5.pack()
boton_6.pack()
boton_7.pack()
boton_8.pack()

ventana_principal.mainloop()
