"""Historial de conversiones válido solo durante la ejecución del programa."""

from validaciones import validar_indice


def registrar_conversion(historial, numero, origen, destino, resultado):
    """Almacena una conversión válida (nunca ejercicios de práctica)."""
    historial.append({
        "numero": numero,
        "origen": origen,
        "destino": destino,
        "resultado": resultado,
    })


def mostrar_historial(historial):
    """Muestra registros numerados y su cantidad total como en la página 8."""
    print("\n" + "=" * 55)
    print("HISTORIAL DE CONVERSIONES")
    print("=" * 55)
    if not historial:
        print("El historial está vacío.")
    else:
        for posicion, registro in enumerate(historial, 1):
            print(f"\nRegistro {posicion}")
            print(f"  Entrada: {registro['numero']}")
            print(f"  Origen: {registro['origen']}")
            print(f"  Destino: {registro['destino']}")
            print(f"  Resultado: {registro['resultado']}")
    print(f"\nTotal de registros: {len(historial)}")


def eliminar_registro(historial):
    """Elimina un registro tras validar su número."""
    if not historial:
        print("El historial está vacío. No hay registros para eliminar.")
        return
    while True:
        texto = input("Número del registro que desea eliminar: ")
        try:
            indice = validar_indice(texto, len(historial))
        except ValueError as error:
            print(f"Error: {error}")
            continue
        eliminado = historial.pop(indice)
        print(
            f"Registro eliminado: {eliminado['numero']} "
            f"({eliminado['origen']}) -> {eliminado['resultado']} "
            f"({eliminado['destino']})."
        )
        return


def vaciar_historial(historial):
    """Vacía todos los registros tras una confirmación."""
    if not historial:
        print("El historial ya está vacío.")
        return
    while True:
        respuesta = input("¿Vaciar TODO el historial? (S/N): ").upper()
        if respuesta == "S":
            historial.clear()
            print("Historial vaciado correctamente.")
            return
        if respuesta == "N":
            print("Vaciado cancelado.")
            return
        print("Error: escriba S o N.")


def menu_historial(historial):
    """Presenta inmediatamente registros y las tres opciones del ejemplo."""
    while True:
        mostrar_historial(historial)
        print("\n1. Eliminar un registro")
        print("2. Vaciar historial")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            eliminar_registro(historial)
        elif opcion == "2":
            vaciar_historial(historial)
        elif opcion == "3":
            return
        else:
            print("Error: seleccione una opción del 1 al 3.")