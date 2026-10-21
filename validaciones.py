BASES = (
    "Binario": 2,
    "Octal": 8,
    "Hexadecimal":16,
)


DIGITOS = "0123456789ABCDEF"
def validar_numero(texto, nombre_base):
    if nombre_base not in BASES:
        raise ValueError("La base seleccionada no es válida.")

    if texto == "":
        raise ValueError("Debe ingresar un número.")

    if len(texto) > 128:
        raise ValueError("Se admiten como máximo 128 dígitos.")
    
    texto = texto.upper()
permitidos = DIGITOS[:BASES[nombre_base]]

for caracter in texto:
    if caracter not in permitidos:
        raise ValueError(
            f"Entrada inválida para {nombre_base}."
            f"Caracteres permitidos: {permitidos}"
        )

return texto
def validar_entrada(texto, origen, destino):
    if origen not in BASES or destino not in BASES:
        raise ValueError("Seleccione bases válidas.")

    if origen == destino:
        raise ValueError(
            "Las bases de origen y destino deben ser diferentes."
        )

    return validar_numero(texto, origen)

def validar_entrada(texto, origen, destino):
    if origen not in BASES or destino not in BASES:
        raise ValueError("Seleccione bases válidas.")

    if origen == destino:
        raise ValueError(
            "Las bases de origen y destino deben ser diferentes."
        )

    return validar_numero(texto, origen)
def validar_indice(texto, cantidad):
    if cantidad == 0:
        raise ValueError("El historial está vacío.")

    if not texto or any(c not in "0123456789" for c in texto):
        raise ValueError("Ingrese el número del registro.")

    # Normalizo ceros iniciales y evito convertir cadena vacía
    normalizado = texto.lstrip("0") or "0"

    if len(normalizado) > len(str(cantidad)):
        raise ValueError("El registro seleccionado no es válido.")

    numero = int(normalizado)

    if numero < 1 or numero > cantidad:
       if numero < 1 or numero > cantidad:
        raise ValueError("El registro seleccionado no existe.")

return numero - 1