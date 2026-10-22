"""Historial en memoria para conversiones hechas desde el menú principal.

Cada registro es un diccionario con numero, origen, destino y resultado.
La lista se crea al iniciar el programa y se elimina al cerrarlo.
"""

from validaciones import validar_indice


def registrar_conversion(historial, numero, origen, destino, resultado):
    """Agrega una conversión válida; los ejercicios de práctica no usan esta función."""
    historial.append({
        "numero": numero,
        "origen": origen,
        "destino": destino,
        "resultado": resultado,
    })


def mostrar_historial(historial):
    """Imprime los registros numerados empezando desde 1."""
    print("\n=== HISTORIAL DE CONVERSIONES ===")
    if not historial:
        print("El historial está vacío.")
        return

    for numero_registro, registro in enumerate(historial, start=1):
        print(
            f"{numero_registro}. {registro['numero']} ({registro['origen']}) "
            f"-> {registro['resultado']} ({registro['destino']})"
        )


def eliminar_registro(historial):
    """Solicita el número de registro y elimina solamente si es válido."""
    if not historial:
        print("El historial está vacío. No hay registros que eliminar.")
        return

    mostrar_historial(historial)
    while True:
        seleccion = input("Número de registro que desea eliminar: ")
        try:
            indice = validar_indice(seleccion, len(historial))
        except ValueError as error:
            print(f"Error: {error}")
        else:
            eliminado = historial.pop(indice)
            print(
                f"Registro eliminado: {eliminado['numero']} "
                f"({eliminado['origen']}) -> {eliminado['resultado']} "
                f"({eliminado['destino']})."
            )
            return


def vaciar_historial(historial):
    """Permite vaciar todo el historial con una confirmación explícita."""
    if not historial:
        print("El historial ya está vacío.")
        return

    while True:
        respuesta = input("¿Desea eliminar TODOS los registros? (S/N): ").upper()
        if respuesta == "S":
            historial.clear()
            print("Historial vaciado correctamente.")
            return
        if respuesta == "N":
            print("Operación cancelada. No se eliminó ningún registro.")
            return
        print("Error: escriba S para confirmar o N para cancelar.")


def menu_historial(historial):
    """Administra el historial y permite volver al menú principal."""
    while True:
        print("\n=== MENÚ DE HISTORIAL ===")
        print("1. Mostrar historial")
        print("2. Eliminar un registro")
        print("3. Vaciar historial")
        print("4. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_historial(historial)
        elif opcion == "2":
            eliminar_registro(historial)
        elif opcion == "3":
            vaciar_historial(historial)
        elif opcion == "4":
            return
        else:
            print("Error: seleccione una opción del 1 al 4.")