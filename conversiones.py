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
    
    return total, pasos

def desde_decimal(numero, base):
    """Convierte un entero no negativo mediante divisiones sucesivas."""
    if numero == 0:
    return "0", [
        "El número es cero.",
        "Su representación en la base de destino es 0.",
    ]

resultado = ""
pasos = []

while numero > 0:
    cociente = numero // base
    residuo = numero % base
    simbolo = DIGITOS[residuo]

    pasos.append(
        f"{numero} / {base}: "
        f"cociente = {cociente}, "
        f"residuo = {residuo}, "
        f"dígito = {simbolo}"
    )
    resultado = simbolo + resultado
numero = cociente

pasos.append(
    "Leer los residuos del último al primero: "
    + resultado
)

return resultado, pasos

#TERMINADO