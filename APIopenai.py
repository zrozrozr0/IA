import re
from random import choice

# Diccionario de palabras clave y respuestas
keywords = {r'(.*) necesito (.*)': ["¿Por qué necesitas {1}?", "¿Realmente necesitas {1}?", "¿Qué pasaría si no tuvieras {1}?"],
            r'(.*) me siento (.*)': ["¿Por qué sientes {1}?", "¿Qué te hace sentir {1}?", "¿Cómo te afecta sentir {1}?"]
            }

# Lista de respuestas genéricas
generic_responses = [
    "Por favor, cuéntame más.",
    "¿Por qué piensas eso?",
    "Entiendo. Sigue hablando.",
    "¿Podrías explicar eso un poco más?",
    "¿Cómo te hace sentir eso?"
]

# Función para procesar la entrada del usuario y producir una respuesta


def eliza():
    print("Hola, soy Eliza. ¿En qué puedo ayudarte hoy?")
    while True:
        user_input = input().lower()
        if user_input == 'salir':
            print("Adiós, ¡espero haberte ayudado!")
            break
        for regex, responses in keywords.items():
            match = re.match(regex, user_input)
            if match:
                response = choice(responses)
                print(response.format(*match.groups()))
                break
        else:
            print(choice(generic_responses))


# Ejecutar el programa
eliza()
