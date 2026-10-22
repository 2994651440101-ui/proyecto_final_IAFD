"""Algoritmos manuales de conversion de sistemas numericos.

No usamos bin(), oct(), hex(), int(texto, base) ni formato de bases.
"""

from validaciones import BASES, DIGITOS


def a_decimal(texto, base):
    """Aplica notacion posicional a un texto previamente validado."""
    total = 0
    pasos = []

    for posicion, caracter in enumerate(reversed(texto)):
        valor = DIGITOS.index(caracter)
        aporte = valor * (base ** posicion)
        total += aporte
        pasos.append(
            f"{caracter} (valor {valor}) x {base}^{posicion} = {aporte}"
        )

    pasos.append(f"Suma de los aportes: {total}")
    return total, pasos


def desde_decimal(numero, base):
    """Convierte un entero no negativo por divisiones sucesivas."""
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
            f"{numero} / {base}: cociente = {cociente}, "
            f"residuo = {residuo}, dígito = {simbolo}"
        )
        resultado = simbolo + resultado
        numero = cociente

    pasos.append("Leer los residuos del último al primero: " + resultado)
    return resultado, pasos


def convertir(texto_validado, origen, destino):
    """Convierte un texto ya validado. Devuelve (resultado, pasos)."""
    base_origen = BASES[origen]
    base_destino = BASES[destino]

    if origen == "Decimal":
        valor_decimal = int(texto_validado)
        pasos_origen = [f"El número ya está en base decimal: {valor_decimal}."]
    else:
        valor_decimal, pasos_origen = a_decimal(texto_validado, base_origen)

    if destino == "Decimal":
        resultado = str(valor_decimal)
        pasos_destino = ["El resultado en base decimal es: " + resultado]
    else:
        resultado, pasos_destino = desde_decimal(valor_decimal, base_destino)

    pasos = [f"Paso 1: convertir desde {origen} a decimal."]
    pasos.extend(pasos_origen)
    pasos.append(f"Paso 2: convertir de decimal a {destino}.")
    pasos.extend(pasos_destino)
    return resultado, pasos