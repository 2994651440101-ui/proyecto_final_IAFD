"""Algoritmos manuales: notación posicional y divisiones sucesivas.

Prohibido sustituirlos por bin(), oct(), hex(), int(texto, base),
o formatos automáticos de cambio de base.
"""

from validaciones import BASES, DIGITOS


def a_decimal(texto_validado, base):
    """Calcula el valor decimal según el peso de cada posición.

    El texto DEBE llegar validado; el orden de los pasos sigue el ejemplo
    de la página 7 del enunciado: de derecha a izquierda (potencias 0, 1, ...).
    """
    total = 0
    pasos = []
    for posicion, caracter in enumerate(reversed(texto_validado)):
        valor_digito = DIGITOS.index(caracter)
        aporte = valor_digito * (base ** posicion)
        total += aporte
        pasos.append(
            f"{caracter} (valor {valor_digito}) x {base}^{posicion} = {aporte}"
        )
    pasos.append(f"Suma de los aportes: {total}")
    return total, pasos


def desde_decimal(numero, base):
    """Convierte a base destino usando división entera y residuos."""
    if numero < 0:
        raise ValueError("Solo se admiten enteros no negativos.")
    if base not in (2, 8, 10, 16):
        raise ValueError("Base numérica no válida.")
    if numero == 0:
        return "0", ["El valor es 0; en la base de destino también es 0."]

    pasos = []
    resultado = ""
    actual = numero
    while actual > 0:
        cociente = actual // base
        residuo = actual % base
        digito = DIGITOS[residuo]
        pasos.append(
            f"{actual} / {base}: cociente = {cociente}, "
            f"residuo = {residuo}, dígito = {digito}"
        )
        resultado = digito + resultado
        actual = cociente
    pasos.append(f"Leer los residuos del último al primero: {resultado}")
    return resultado, pasos


def convertir(texto_validado, origen, destino):
    """Devuelve (texto_resultado, pasos) para dos bases distintas.

    La entrada debe validarse previamente con validar_entrada().
    """
    if origen not in BASES or destino not in BASES or origen == destino:
        raise ValueError("Las bases de origen y destino deben ser distintas y válidas.")

    pasos = []
    if origen == "Decimal":
        numero_decimal = int(texto_validado)
    else:
        numero_decimal, detalle = a_decimal(texto_validado, BASES[origen])
        if destino != "Decimal":
            pasos.append(f"ETAPA 1: {origen.upper()} A DECIMAL")
        else:
            pasos.append(f"CONVERSIÓN: {origen.upper()} A DECIMAL")
        pasos.extend(detalle)

    if destino == "Decimal":
        resultado = str(numero_decimal)
    else:
        resultado, detalle = desde_decimal(numero_decimal, BASES[destino])
        if origen != "Decimal":
            pasos.append(f"ETAPA 2: DECIMAL A {destino.upper()}")
        else:
            pasos.append(f"CONVERSIÓN: DECIMAL A {destino.upper()}")
        pasos.extend(detalle)

    pasos.append(f"Resultado final en {destino}: {resultado}")
    return resultado, pasos