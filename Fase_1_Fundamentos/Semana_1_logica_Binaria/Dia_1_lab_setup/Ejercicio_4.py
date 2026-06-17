viejo = ["A", "B", "C"]

nuevo = ["A", "X"]

historial_cambio = []


def calcular_diff_lineal(archivo_viejo, archivo_nuevo):

    limite_viejo = 0
    for longitud in viejo:
        limite_viejo += 1

    limite_nuevo = 0
    for longitud in nuevo:
        limite_nuevo += 1

    historial_cambio = []
    p_viejo = 0
    p_nuevo = 0

    while (p_viejo < limite_viejo) and (p_nuevo < limite_nuevo):
        if viejo[p_viejo] == nuevo[p_nuevo]:
            p_nuevo += 1
            p_viejo += 1
        else:
            historial_cambio.append(("DEL", viejo[p_viejo]))
            historial_cambio.append(("ADD", nuevo[p_nuevo]))

        while p_viejo < limite_viejo:
            historial_cambio.append(("DEL", viejo[p_viejo]))
            p_viejo += 1

        while p_nuevo < limite_nuevo:
            historial_cambio.append(("ADD", nuevo[p_nuevo]))
            p_nuevo += 1

    print(historial_cambio)


calcular_diff_lineal(viejo, nuevo)
