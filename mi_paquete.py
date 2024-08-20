from datetime import datetime
import random


def saludar_clase():
    """Función que lee la fecha y hora para devolvertelas con un amigable mensaje
    """
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M")
    print(f"Hola clase! Hoy {fecha}, son las {hora}")




def lanzar_moneda():
    """Función que lanza una moneda y te devuelve el resultado del lanzamiento

    Returns:
        str: Resultado de la moneda (Aguila o Sol)
    """
    resultado = random.choice(["Aguila", "Sol"])
    print(f"¡Lanzaste la moneda y salió: {resultado}!")
    return resultado

