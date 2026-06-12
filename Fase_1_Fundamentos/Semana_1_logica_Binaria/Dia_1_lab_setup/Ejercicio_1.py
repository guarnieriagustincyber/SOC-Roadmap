def segmentar_ruta(cadena_ruta):
    componentes = []
    acumulador = ""
    for caracter in cadena_ruta:
        if caracter != "/":
            acumulador += caracter
        else:
            componentes.append(acumulador)
            acumulador = ""

    if acumulador != "":
        componentes.append(acumulador)

    return componentes


resultado = segmentar_ruta("sys/logs/soc/alert.log")
print(resultado)
