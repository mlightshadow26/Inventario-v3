import tkinter as tk
import time

def funcion_salir():
    ventana_principal.quit()


ventana_principal = tk.Tk()
ventana_principal.title("Control de inventario Py")
ventana_principal.config(background="beige")

ventana_principal.geometry("600x400")



# Bienvenida y otras etiquetas
label_bienvenida = tk.Label(
    text="Bienvenida(o) al Control de Inventario", font=('Consolas', 20)
)
label_bienvenida.pack(pady=10)

label_en_desarrollo = tk.Label(
    ventana_principal,
    text="Esta herramienta aún está en desarrollo",
    font=('Consolas', 14),
)

# Se definen las funciones principales


def limpiar_widgets():
    for widget in ventana_principal.winfo_children():
        widget.pack_forget()


def volver_al_menu_principal():
    limpiar_widgets()
    label_bienvenida.pack(pady=10)
    boton_inventario.pack(pady=5)
    boton_calculos.pack(pady=5)
    boton_cerrar.pack(pady=5, side="bottom")
    print("menu principal")


def empaquetar_botones_inventario():
    limpiar_widgets()
    print("Clean view")
    boton_agregar_inventario.pack(pady=5)
    boton_modificar_inventario.pack(pady=5)
    boton_eliminar_inventario.pack(pady=5)
    boton_menu_principal.pack(pady=10)
    print("menu inventario")


def mensaje_funcionalidad_en_desarrollo():
    label_en_desarrollo.pack_forget()
    time.sleep(1)   
    label_en_desarrollo.pack()


def empaquetar_botones_calculos():
    limpiar_widgets()
    # por implementar
    boton_menu_principal.pack(pady=10)
    mensaje_funcionalidad_en_desarrollo()
    print("menu cálculos")


# Botones menu principal
boton_inventario = tk.Button(
    text="Inventario",
    font=('Consolas', 18),
    command=empaquetar_botones_inventario
)
boton_calculos = tk.Button(
    text="Cálculos de Producción",
    font=('Consolas', 18),
    command=empaquetar_botones_calculos
)
boton_cerrar = tk.Button(
    text="Salir",
    font=('Consolas', 14),
    command=funcion_salir
)
boton_menu_principal = tk.Button(
    text="Volver al menú principal",
    font=('Consolas', 14),
    command=volver_al_menu_principal
)
# Botones del inventario
boton_agregar_inventario = tk.Button(
    text="Agregar item",
    font=('Consolas', 18),
    # command=formulario_agregar
    command=mensaje_funcionalidad_en_desarrollo
)
boton_modificar_inventario = tk.Button(
    text="Modificar item",
    font=('Consolas', 18),
    # command=formulario_modificar
    command=mensaje_funcionalidad_en_desarrollo
)
boton_eliminar_inventario = tk.Button(
    text="Eliminar item",
    font=('Consolas', 18),
    # command=formulario_eliminar
    command=mensaje_funcionalidad_en_desarrollo
)


# Se empaquetan los botones principales
boton_inventario.pack(pady=5)
boton_calculos.pack(pady=5)
boton_cerrar.pack(pady=5, side="bottom")


# Mainloop
ventana_principal.mainloop()
