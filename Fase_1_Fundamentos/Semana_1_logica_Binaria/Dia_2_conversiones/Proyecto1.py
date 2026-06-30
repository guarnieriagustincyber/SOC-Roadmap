def complemento(x):
    carreo = False
    for bit in x:




def decimal_a_binario(n):
    valor_binario = []
    cociente = n
    cantidad = 0
    binario = []

    if n == 0:
        return "0000"
    elif n >= -128 and n <= 127:  # 8 bits
        while cociente > 0:
            resuido = cociente % 2
            cociente = cociente // 2
            valor_binario.append(resuido)
            cantidad =+ 1
        return valor_binario
        cantidad =- 1
        while cantidad >= 0:
            if valor_binario[cantidad] == 0:
                binario.append(1)
            else:
                binario.append(0)





    else:
        return "Fuera de rango"


resultado = decimal_a_binario(10)
print(resultado)
