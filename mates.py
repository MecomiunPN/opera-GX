#inicio
import random

# Definimos una lista de preguntas, respuestas y opciones.
preguntas = [
    {
        "pregunta": "¿Cuál es el resultado de 5 + 7?",
        "opciones": ["A) 10", "B) 12", "C) 8", "D) 15"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Si x = 3, ¿cuál es el valor de 2x - 1?",
        "opciones": ["A) 6", "B) 5", "C) 7", "D) 9"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "Resuelve la ecuación: 2x + 3 = 11",
        "opciones": ["A) x = 4", "B) x = 6", "C) x = 7", "D) x = 5"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el área de un triángulo con base 4 y altura 5?",
        "opciones": ["A) 8", "B) 10", "C) 15", "D) 20"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "Si un número es divisible por 2 y 3, ¿cuál es su mínimo común múltiplo?",
        "opciones": ["A) 2", "B) 3", "C) 6", "D) 9"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es el resultado de 6^2 (6 al cuadrado)?",
        "opciones": ["A) 12", "B) 36", "C) 18", "D) 72"],
        "respuesta_correcta": "B"
    }
    
]

# Función para mostrar y verificar respuestas.
def jugar_preguntas():
    random.shuffle(preguntas)
    puntaje = 0

    for pregunta in preguntas:
        print("\n" + pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta = input("Elije la opción correcta (A, B, C, o D): ").upper()

        if respuesta == pregunta["respuesta_correcta"]:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print("Incorrecto. La respuesta correcta era", pregunta["respuesta_correcta"], "\n")

    print("Tu puntaje final es:", puntaje, "de 6 preguntas.")

# Iniciar el juego.
print("¡Bienvenido al juego matemático!")
jugar_preguntas()
