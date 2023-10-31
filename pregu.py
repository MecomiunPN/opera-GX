import tkinter as tk
import random

# Definir las preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?",
        "opciones": ["1776", "1789", "1801", "1812"],
        "respuesta": "1776",
        "categoria": "Historia"
    },
    {
        "pregunta": "¿Cuál es el deporte más popular en Brasil?",
        "opciones": ["Fútbol", "Baloncesto", "Tenis", "Voleibol"],
        "respuesta": "Fútbol",
        "categoria": "Deporte"
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "opciones": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
        "respuesta": "Leonardo da Vinci",
        "categoria": "Arte"
    },
    {
        "pregunta": "¿Cuál de estos es un género musical?",
        "opciones": ["Python", "Rock", "Matemáticas", "Historia"],
        "respuesta": "Rock",
        "categoria": "Música"
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "opciones": ["Sídney", "Melbourne", "Canberra", "Brisbane"],
        "respuesta": "Canberra",
        "categoria": "Geografía"
    },
    {
        "pregunta": "¿Cuál es el proceso mediante el cual las plantas producen su propio alimento?",
        "opciones": ["Respiración", "Fotosíntesis", "Crecimiento", "Reproducción"],
        "respuesta": "Fotosíntesis",
        "categoria": "Biología"
    },
    {
        "pregunta": "¿Cuál es el hueso más largo del cuerpo humano?",
        "opciones": ["Fémur", "Húmero", "Tibia", "Fibula"],
        "respuesta": "Fémur",
        "categoria": "Anatomía"
    }
]

# Función para seleccionar una pregunta aleatoria
def seleccionar_pregunta():
    return random.choice(preguntas)

# Función para mostrar una pregunta en la ventana
def mostrar_pregunta():
    pregunta_actual = seleccionar_pregunta()
    pregunta_label.config(text=pregunta_actual["pregunta"])
    
    for i in range(4):
        opcion_buttons[i].config(text=pregunta_actual["opciones"][i], command=lambda respuesta=pregunta_actual["opciones"][i]: verificar_respuesta(respuesta))

# Función para verificar la respuesta
def verificar_respuesta(respuesta):
    pregunta_actual = pregunta_label.cget("text")
    for pregunta in preguntas:
        if pregunta["pregunta"] == pregunta_actual:
            if pregunta["respuesta"] == respuesta:
                resultado_label.config(text="¡Correcto!", fg="green")
            else:
                resultado_label.config(text=f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}", fg="red")
    mostrar_pregunta()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Preguntados")
ventana.geometry("400x300")

# Etiqueta para mostrar la pregunta
pregunta_label = tk.Label(ventana, text="", font=("Arial", 12), wraplength=380, justify="center")
pregunta_label.pack(pady=20)

# Botones para las opciones de respuesta
opcion_buttons = []
for i in range(4):
    boton = tk.Button(ventana, text="", font=("Arial", 10))
    boton.pack()
    opcion_buttons.append(boton)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack()

# Botón para comenzar el juego
iniciar_button = tk.Button(ventana, text="Comenzar", font=("Arial", 12), command=mostrar_pregunta)
iniciar_button.pack()

ventana.mainloop()

