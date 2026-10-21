from validaciones import DIGITOS

def a_decimal(texto, base):
    """Convierte una cadena validada a un entero decimal."""
    total = 0
    pasos = []

    for posicion, caracter in enumerate(reversed(texto)):
        valor = DIGITOS.index(caracter)
        aporte = valor * (base ** posicion)
        total += aporte

        pasos.append(
            f"{caracter} (valor {valor}) x "
            f"{base}^{posicion} = {aporte}"
        )

    pasos.append(f"Suma de los aportes: {total}")