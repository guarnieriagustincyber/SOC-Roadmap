def decimal_a_binario(decimal):
    binario_str = ""
    contador = 0
    if decimal == "0":
        return "0000000000000000"
    while decimal > 0:

        resuido = decimal % 2
        binario_str = str(resuido) + binario_str
        decimal = decimal // 2
        contador += 1

    while contador < 16:
        binario_str = "0" + binario_str
        contador += 1

    return binario_str


def aislar_bits(binario_str):
    byte_alto = ""
    i = 0
    while i < 8:
        byte_alto += binario_str[i]
        i += 1

    byte_bajo = ""
    j = 8
    while j < 16:
        byte_bajo += binario_str[j]
        j += 1

    return byte_alto, byte_bajo


def binario_a_hexadecimal(binario_str):
    conversor = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    valor_Hex = ""
    indice = 0
    while indice < 16:
        nibble = ""
        k = 0
        while k < 4:
            nibble += binario_str[indice + k]
            k += 1
        valor_Hex += conversor[nibble]
        indice += 4
    return valor_Hex


def __main__(decimal):
    print(f"Dato Decimal: {decimal}")

    trama_binaria = decimal_a_binario(decimal)
    print(f"Trama Binaria (16-bit): {trama_binaria}")

    b_alto, b_bajo = aislar_bits(trama_binaria)
    print(f"Byte Alto (MSB): {b_alto}")
    print(f"Byte Bajo (LSB): {b_bajo}")

    volcado_hex = binario_a_hexadecimal(trama_binaria)
    print(f"Volcado Hexadecimal: {volcado_hex}")


# --- Flujo de Control de Entrada Sólido ---
intentos = 3
exito = False
valor_final = 0

while intentos > 0:
    entrada = input("Ingrese el valor decimal que quiere convertir (0 - 65535): ")

    # Validar que la entrada sea numérico puro antes de castear
    es_numero = True
    for caracter in entrada:
        if caracter < "0" or caracter > "9":
            es_numero = False

    if es_numero and entrada != "":
        valor_final = int(entrada)
        if 0 <= valor_final <= 65535:
            exito = True
            break

    intentos -= 1
    print(f"Número fuera de rango o inválido. Intentos restantes: {intentos}")

if exito:
    __main__(valor_final)
else:
    print("Error Crítico: Acceso denegado por reiteración de fallas en los datos.")
