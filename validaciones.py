"""Validación de enteros no negativos escritos en bases 2, 8, 10 o 16.

La validación se hace ANTES de cualquier conversión, sin quitar espacios.
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
    """Devuelve el texto normalizado o lanza ValueError si no es válido."""
    if nombre_base not in BASES:
        raise ValueError("La base seleccionada no es válida.")
    if not texto:
        raise ValueError("Debe ingresar un número; la entrada está vacía.")
    if len(texto) > MAX_DIGITOS:
        raise ValueError(f"Se admiten como máximo {MAX_DIGITOS} dígitos.")

    permitidos = DIGITOS[:BASES[nombre_base]]
    # Validar caracteres ORIGINALES para impedir equivalencias Unicode engañosas
    # (por ejemplo, ligaduras que al pasarlas a mayúsculas producen dos letras).
    permitidos_originales = permitidos
    if nombre_base == "Hexadecimal":
        permitidos_originales += "abcdef"
    for caracter in texto:
        if caracter not in permitidos_originales:
            raise ValueError(
                f"El carácter {caracter!r} no es válido en {nombre_base}. "
                f"Solo se permiten los dígitos: {permitidos}."
            )
    return texto.upper()


def validar_entrada(texto, origen, destino):
    """Comprueba ambas bases y valida un número escrito en la base origen."""
    if origen not in BASES or destino not in BASES:
        raise ValueError("Seleccione bases de origen y destino válidas.")
    if origen == destino:
        raise ValueError("Las bases de origen y destino deben ser diferentes.")
    return validar_numero(texto, origen)


def validar_indice(texto, cantidad):
    """Convierte un número de registro 1..N a índice 0..N-1."""
    if cantidad <= 0:
        raise ValueError("El historial está vacío.")
    if not texto or any(caracter not in '0123456789' for caracter in texto):
        raise ValueError("Ingrese un número de registro válido.")
    # Evita transformar entradas absurdamente extensas a enteros.
    sin_ceros = texto.lstrip('0') or '0'
    if len(sin_ceros) > len(str(cantidad)):
        raise ValueError("El registro seleccionado no existe.")
    numero = int(sin_ceros)
    if not 1 <= numero <= cantidad:
        raise ValueError("El registro seleccionado no existe.")
    return numero - 1