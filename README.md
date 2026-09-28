import tkinter as tk
from tkinter import messagebox

# Intentamos importar los módulos conforme los vayas creando.
# Si el archivo aún no existe, el programa capturará el error para no cerrarse.

def abrir_trabajo_1():
    try:
        import trabajo1
        trabajo1.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 1 aún no ha sido agregado.")

def abrir_trabajo_2():
    try:
        import trabajo2
        trabajo2.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 2 aún no ha sido agregado.")

def abrir_trabajo_3():
    try:
        import trabajo3
        trabajo3.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 3 aún no ha sido agregado.")

def abrir_trabajo_4():
    try:
        import trabajo4
        trabajo4.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 4 aún no ha sido agregado.")

def abrir_trabajo_5():
    try:
        import trabajo5
        trabajo5.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 5 aún no ha sido agregado.")

def abrir_trabajo_6():
    try:
        import trabajo6
        trabajo6.abrir_ventana(root)
    except ModuleNotFoundError:
        messagebox.showinfo("En desarrollo", "El Trabajo 6 aún no ha sido agregado.")


# Configuración de la Ventana Principal
root = tk.Tk()
root.title("Menú de Proyectos Python")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# Encabezado
lbl_titulo = tk.Label(
    root, 
    text="Portafolio de Proyectos", 
    font=("Helvetica", 18, "bold"), 
    fg="#cdd6f4", 
    bg="#1e1e2e"
)
lbl_titulo.pack(pady=20)

lbl_subtitulo = tk.Label(
    root, 
    text="Selecciona el trabajo que deseas ejecutar:", 
    font=("Helvetica", 10), 
    fg="#a6adc8", 
    bg="#1e1e2e"
)
lbl_subtitulo.pack(pady=(0, 20))

# Marco contenedor de botones
frame_botones = tk.Frame(root, bg="#1e1e2e")
frame_botones.pack(pady=10)

# Estilos de botones
estilo_bot = {
    "font": ("Helvetica", 11, "bold"),
    "bg": "#89b4fa",
    "fg": "#11111b",
    "activebackground": "#b4befe",
    "activeforeground": "#11111b",
    "width": 25,
    "bd": 0,
    "pady": 8,
    "cursor": "hand2"
}

# Lista de botones
btn_t1 = tk.Button(frame_botones, text="Trabajo 1", command=abrir_trabajo_1, **estilo_bot)
btn_t1.pack(pady=6)

btn_t2 = tk.Button(frame_botones, text="Trabajo 2", command=abrir_trabajo_2, **estilo_bot)
btn_t2.pack(pady=6)

btn_t3 = tk.Button(frame_botones, text="Trabajo 3", command=abrir_trabajo_3, **estilo_bot)
btn_t3.pack(pady=6)

btn_t4 = tk.Button(frame_botones, text="Trabajo 4", command=abrir_trabajo_4, **estilo_bot)
btn_t4.pack(pady=6)

btn_t5 = tk.Button(frame_botones, text="Trabajo 5", command=abrir_trabajo_5, **estilo_bot)
btn_t5.pack(pady=6)

btn_t6 = tk.Button(frame_botones, text="Trabajo 6", command=abrir_trabajo_6, **estilo_bot)
btn_t6.pack(pady=6)

# Pie de página
lbl_footer = tk.Label(
    root, 
    text="Desarrollado en Python & Tkinter", 
    font=("Helvetica", 8, "italic"), 
    fg="#6c7086", 
    bg="#1e1e2e"
)
lbl_footer.pack(side="bottom", pady=15)

# Bucle principal de la interfaz
root.mainloop()