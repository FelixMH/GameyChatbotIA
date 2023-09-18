# Importamos las librerías de TKinter.
import tkinter as tk
from tkinter import Scrollbar, PhotoImage
from Chatbot import chatbot

from PIL import Image

from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkTextbox


# Creación de una ventana
ventana = CTk()
ventana.title("Gamey - Tu chatbot inteligente")

# colores
c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_blanco = "#ffffff"
c_verde_hover = "#1A5D1A"

# Asignarle el ancho de la ventana
ventana.geometry("1200x780+250+20")
# ventana.minsize(600, 300)
ventana.config(bg=c_negro)

# logo
logo = PhotoImage(file='images/icono.png')

# Configuración del icono de la ventana
ventana.iconphoto(True, logo)


# ventana frame para el chat, y demás
frame = CTkFrame(ventana, fg_color=c_negro,
                 border_color=c_verde, border_width=2)
frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# label para icono
my_image = CTkImage(light_image=Image.open('./images/icono.png'),
                    dark_image=Image.open('./images/icono.png'),
                    size=(150, 150))

icono = CTkLabel(frame, image=my_image, text="",
                 compound="center", anchor="center")

icono.grid(row=0, padx=10, pady=10)

text_icon = CTkLabel(frame, image=None, text="Gamey - Chatbot",
                     compound="center", anchor="center", font=('verdana', 20))

text_icon.grid(row=1, padx=10, pady=10)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Creación de un widget de chat para las respuestas y preguntas.
chat = CTkTextbox(
    frame,
    width=600,
    height=300,
    activate_scrollbars=True,
    fg_color=c_negro,
    font=('verdana', 16)
)

chat.grid(columnspan=4, row=2, sticky="ew")


# Creación de un campo de texto para hacerle una pregunta al chatbot.
txt_pregunta = CTkEntry(
    ventana,
    width=120,
    height=40,
    border_color=c_verde,
    placeholder_text="Escribe tu pregunta....",
    font=('Verdana', 16)
)

txt_pregunta.grid(columnspan=4, row=3, sticky="nsew", padx=10, pady=10)


def preguntar():
    pregunta = txt_pregunta.get()
    agregar_mensaje(f"Tú: {pregunta}"+"\n")
    respuesta = obtener_respuesta(pregunta)
    agregar_mensaje(f"Chatbot: {respuesta}" + "\n")
    txt_pregunta.delete(0, tk.END)


def agregar_mensaje(mensaje):
    # chat.config(state=tk.NORMAL)
    chat.configure(state=tk.NORMAL)
    chat.insert(
        tk.END,
        f"{mensaje} \n",
    )
    chat.configure(state=tk.DISABLED)


def obtener_respuesta(mensaje):
    return chatbot.get_response(mensaje)


# Creación de un botón para enviar los mensajes.
boton_enviar = CTkButton(
    ventana,
    text="Preguntar",
    command=preguntar,
    fg_color=c_verde_hover,
    text_color=c_blanco,
    border_color=c_blanco,
    hover_color=c_verde,
    font=('verdana', 20)
)

boton_enviar.grid(column=0, row=4, sticky="ew", padx=8, pady=8)


# Iniciar la aplicación de escritorio
ventana.call('wm', 'iconphoto', ventana._w, logo)
ventana.mainloop()
