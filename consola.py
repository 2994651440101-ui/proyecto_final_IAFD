"""Interfaz principal de consola: menús, datos y navegación."""

from validaciones import BASES, validar_entrada
from conversiones import convertir
from historial import registrar_conversion, menu_historial
from practica import crear_puntuacion, menu_practica

NOMBRES_BASES = list(BASES)


def seleccionar_base(titulo, base_excluida=None):
    """Muestra bases disponibles; devuelve None cuando se elige 0."""
    while True:
        print("\n" + "=" * 55)
        print(titulo)
        print("=" * 55)
        for numero, nombre in enumerate(NOMBRES_BASES, start=1):
            if nombre != base_excluida:
                print(f"{numero}. {nombre}")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return None
        if opcion in ("1", "2", "3", "4"):
            base = NOMBRES_BASES[int(opcion) - 1]
            if base != base_excluida:
                return base
            print("Error: el destino debe ser diferente al origen.")
        else:
            print("Error: seleccione una opción disponible.")


def menu_conversion(historial):
    """Gestiona una conversión o permite cancelarla en cualquier selección."""
    origen = seleccionar_base("SELECCIONE LA BASE DE ORIGEN")
    if origen is None:
        return
    destino = seleccionar_base("SELECCIONE LA BASE DE DESTINO", origen)
    if destino is None:
        return

    print("\n" + "=" * 55)
    print(f"CONVERSIÓN: {origen.upper()} A {destino.upper()}")
    print("=" * 55)
    print("Ingrese un entero no negativo de hasta 128 dígitos.")
    print("Escriba 'volver' para regresar al menú principal.")
    while True:
        original = input("\nNúmero a convertir: ")
        if original.lower() == "volver":
            print("Conversión cancelada.")
            return
        try:
            normalizado = validar_entrada(original, origen, destino)
        except ValueError as error:
            print(f"Error: {error}")
            continue
        break

    resultado, pasos = convertir(normalizado, origen, destino)
    print("\n" + "=" * 55)
    print("RESULTADO")
    print("=" * 55)
    print(f"Número ingresado: {original}")
    print(f"Base de origen: {origen}")
    print(f"Base de destino: {destino}")
    print(f"Resultado: {resultado}")

    print("\n" + "=" * 55)
    print("PROCEDIMIENTO PASO A PASO")
    print("=" * 55)
    for paso in pasos:
        print(paso)

    registrar_conversion(historial, original, origen, destino, resultado)
    print("\nConversión agregada al historial.")
    input("\nPresione Enter para continuar...")


def iniciar_programa():
    """Inicia la aplicación; conserva listas y puntuación mientras esté abierta."""
    historial = []
    puntuacion = crear_puntuacion()
    while True:
        print("\n" + "=" * 55)
        print("CONVERSOR DE SISTEMAS NUMÉRICOS")
        print("=" * 55)
        print("1. Realizar una conversión")
        print("2. Consultar el historial")
        print("3. Iniciar el modo de práctica")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            menu_conversion(historial)
        elif opcion == "2":
            menu_historial(historial)
        elif opcion == "3":
            menu_practica(puntuacion)
        elif opcion == "4":
            print("Programa finalizado. ¡Hasta pronto!")
            return
        else:
            print("Error: seleccione una opción del 1 al 4.")