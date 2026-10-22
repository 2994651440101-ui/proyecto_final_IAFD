"""Validaciones del conversor de sistemas numéricos.

Todas las entradas de números se validan como texto ANTES de convertirlas.
Se admiten únicamente números enteros no negativos de hasta 128 dígitos.
"""

BASES = {
    "Binario": 2,
    "Octal": 8,
    "Decimal": 10,
    "Hexadecimal": 16,
}

DIGITOS = "0123456789ABCDEF"
MAX_DIGITOS = 128


def validar_numero(texto, nombre_base):
    """Devuelve el número normalizado a mayúsculas o lanza ValueError."""
    if nombre_base not in BASES:
        raise ValueError("La base seleccionada no es válida.")

    if texto == "":
        raise ValueError("Debe ingresar un número; la entrada no puede estar vacía.")

    if len(texto) > MAX_DIGITOS:
        raise ValueError(f"Se admiten como máximo {MAX_DIGITOS} dígitos.")

    permitidos = DIGITOS[:BASES[nombre_base]]
    texto_normalizado = texto.upper()
    for caracter in texto_normalizado:
        if caracter not in permitidos:
            raise ValueError(
                f"El carácter {caracter!r} no es válido para {nombre_base}. "
                f"Se permiten únicamente: {permitidos}."
            )

    return texto_normalizado


def validar_entrada(texto, origen, destino):
    """Comprueba que las bases sean diferentes y valida el número de origen."""
    if origen not in BASES or destino not in BASES:
        raise ValueError("Seleccione bases de origen y destino válidas.")

    if origen == destino:
        raise ValueError("Las bases de origen y destino deben ser diferentes.")

    return validar_numero(texto, origen)


def validar_indice(texto, cantidad):
    """Devuelve índice de lista (desde cero) para un registro numerado desde uno."""
    if cantidad <= 0:
        raise ValueError("El historial está vacío.")

    if texto == "" or any(caracter not in "0123456789" for caracter in texto):
        raise ValueError("Ingrese un número de registro válido.")

    normalizado = texto.lstrip("0") or "0"
    if len(normalizado) > len(str(cantidad)):
        raise ValueError("El registro seleccionado no existe.")

    numero = int(normalizado)
    if numero < 1 or numero > cantidad:
        raise ValueError("El registro seleccionado no existe.")

    return numero - 1