import random
import string

# Aquí se ingresa el mensaje de bienvenida al usuario
print("Hola, estás usando el siguiente programa que te ayudará a crear una contraseña segura.")
print("A continuación, agrega un número que definirá la longitud de la contraseña.")
print("El mínimo permitido es 8 dígitos.\n") 

# En esta seccion se le pedira al usuario cuantos digitos desea
n = int(input("¿Cuántos dígitos quieres para la contraseña? (mínimo 8): "))

def generar_contrasena(longitud):
    if longitud < 8:
        print("La longitud mínima es 8.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print("Tu contraseña es:", generar_contrasena(n))


# =========================
# INTERFAZ GRÁFICA (AGREGADO)
# =========================

import tkinter as tk
from tkinter import messagebox

def generar_desde_gui():
    try:
        longitud = int(entry_longitud.get())
        resultado = generar_contrasena(longitud)
        if resultado:
            resultado_var.set(resultado)
        else:
            resultado_var.set("")
            messagebox.showwarning("Error", "La longitud mínima es 8.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("420x300")
ventana.configure(bg="black")
ventana.resizable(False, False)

# Fuente tipo hacker
fuente_titulo = ("Consolas", 14, "bold")
fuente_texto = ("Consolas", 11)

# Título
label_titulo = tk.Label(
    ventana,
    text="GENERADOR DE CONTRASEÑAS SEGURAS",
    fg="#00ff00",
    bg="black",
    font=fuente_titulo
)
label_titulo.pack(pady=15)

# Entrada de longitud
label_longitud = tk.Label(
    ventana,
    text="Longitud (mínimo 8):",
    fg="#00ff00",
    bg="black",
    font=fuente_texto
)
label_longitud.pack()

entry_longitud = tk.Entry(
    ventana,
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    font=fuente_texto,
    justify="center"
)
entry_longitud.pack(pady=5)

# Botón generar
btn_generar = tk.Button(
    ventana,
    text="GENERAR CONTRASEÑA",
    command=generar_desde_gui,
    bg="black",
    fg="#00ff00",
    activebackground="#003300",
    activeforeground="#00ff00",
    font=fuente_texto,
    borderwidth=2,
    relief="ridge"
)
btn_generar.pack(pady=15)

# Resultado
resultado_var = tk.StringVar()

label_resultado = tk.Label(
    ventana,
    textvariable=resultado_var,
    fg="#00ff00",
    bg="black",
    font=("Consolas", 10),
    wraplength=380,
    justify="center"
)
label_resultado.pack(pady=10)

ventana.mainloop()
))
