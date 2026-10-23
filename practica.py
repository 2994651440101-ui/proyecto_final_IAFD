"""Ejercicios aleatorios y puntuación que persiste durante la ejecución."""

import random

from validaciones import BASES, validar_numero
from conversiones import a_decimal, desde_decimal


def crear_puntuacion():
    """Devuelve el estado inicial compartido con el menú principal."""
    return {"aciertos": 0, "respondidos": 0}


def porcentaje_aciertos(puntuacion):
    """Evita división por cero antes del primer ejercicio."""
    if puntuacion["respondidos"] == 0:
        return 0.0
    return puntuacion["aciertos"] * 100 / puntuacion["respondidos"]


def mostrar_puntuacion(puntuacion):
    print(f"Aciertos: {puntuacion['aciertos']}")
    print(f"Ejercicios respondidos: {puntuacion['respondidos']}")
    print(f"Porcentaje de aciertos: {porcentaje_aciertos(puntuacion):.1f}%")


def generar_ejercicio():
    """Genera (decimal, origen, destino, entrada, respuesta) con 0 <= valor <= 255."""
    decimal = random.randint(0, 255)
    origen, destino = random.sample(list(BASES), 2)
    entrada, _ = desde_decimal(decimal, BASES[origen])
    respuesta, _ = desde_decimal(decimal, BASES[destino])
    return decimal, origen, destino, entrada, respuesta


def resolver_ejercicio(puntuacion):
    """Acepta una sola respuesta válida; errores de formato no puntúan."""
    valor, origen, destino, entrada, respuesta_esperada = generar_ejercicio()
    print("\n" + "=" * 55)
    print("EJERCICIO DE PRÁCTICA")
    print("=" * 55)
    print(f"Convierta {entrada} de {origen} a {destino}.")
    print("\nIngrese únicamente el número de la respuesta.")

    while True:
        texto = input("Su respuesta: ")
        try:
            respuesta_validada = validar_numero(texto, destino)
        except ValueError as error:
            print(f"Error: {error}")
            continue
        break

    # Comparamos por valor, no por forma: FF == ff == 0FF en hexadecimal.
    if destino == "Decimal":
        valor_respuesta = int(respuesta_validada)
    else:
        valor_respuesta, _ = a_decimal(respuesta_validada, BASES[destino])

    correcta = valor_respuesta == valor
    puntuacion["respondidos"] += 1
    if correcta:
        puntuacion["aciertos"] += 1
        print("\n¡Respuesta correcta!")
    else:
        print(f"\nRespuesta incorrecta. La respuesta correcta es: {respuesta_esperada}")
    print()
    mostrar_puntuacion(puntuacion)
    input("\nPresione Enter para continuar...")
    return correcta


def menu_practica(puntuacion):
    """Permite volver sin perder los aciertos de esta misma sesión."""
    while True:
        print("\n" + "=" * 55)
        print("MODO DE PRÁCTICA")
        print("=" * 55 + "\n")
        mostrar_puntuacion(puntuacion)
        print("\n1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            resolver_ejercicio(puntuacion)
        elif opcion == "2":
            puntuacion["aciertos"] = 0
            puntuacion["respondidos"] = 0
            print("Puntuación reiniciada correctamente.")
        elif opcion == "3":
            return
        else:
            print("Error: seleccione una opción del 1 al 3.")