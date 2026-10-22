"""Menús en consola del conversor de sistemas numéricos."""

from validaciones import BASES, validar_entrada
from conversiones import convertir
from historial import registrar_conversion, menu_historial


NOMBRES_BASES = list(BASES)


def seleccionar_base(mensaje):
    """Pide una base y repite si la opción no es válida."""
    while True:
        print("\nSISTEMAS NUMÉRICOS")
        for posicion, nombre in enumerate(NOMBRES_BASES, start=1):
            print(f"{posicion}. {nombre} (base {BASES[nombre]})")

        seleccion = input(mensaje).strip()
        if seleccion in ("1", "2", "3", "4"):
            return NOMBRES_BASES[int(seleccion) - 1]
        print("Error: seleccione una opción del 1 al 4.")


def menu_conversion(historial):
    """Selecciona bases, valida la entrada y muestra resultado y procedimiento."""
    print("\n=== REALIZAR UNA CONVERSIÓN ===")
    origen = seleccionar_base("Seleccione la base de origen: ")

    while True:
        destino = seleccionar_base("Seleccione la base de destino: ")
        if origen != destino:
            break
        print("Error: la base de destino debe ser diferente a la de origen.")

    while True:
        texto = input(f"Ingrese un número en {origen}: ")
        try:
            numero_validado = validar_entrada(texto, origen, destino)
            break
        except ValueError as error:
            print(f"Error: {error}")

    resultado, pasos = convertir(numero_validado, origen, destino)
    print("\n=== RESULTADO ===")
    print(f"Número ingresado: {numero_validado}")
    print(f"Base de origen: {origen} ({BASES[origen]})")
    print(f"Base de destino: {destino} ({BASES[destino]})")
    print(f"Resultado: {resultado}")

    print("\n=== PROCEDIMIENTO PASO A PASO ===")
    for paso in pasos:
        print(paso)
    registrar_conversion(historial, numero_validado, origen, destino, resultado)
    print("\nRegresando al menú principal...")


def iniciar_programa():
    """Ejecuta el menú principal hasta que se seleccione Salir."""
    historial = []
    while True:
        print("\n===== CONVERSOR DE SISTEMAS NUMÉRICOS =====")
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
            print("\nEl modo de práctica estará disponible en una etapa posterior.")
        elif opcion == "4":
            print("\nGracias por usar el conversor. ¡Hasta pronto!")
            return
        else:
            print("Error: seleccione una opción del 1 al 4.")