entrada = [
    ["fase_1", "semana_1", "script.py"],
    ["fase_1", "readme.md"],
    ["docs", "manual.txt"],
]


def construir_estructura_directorio(lista_rutas):
    raiz = {}

    for linea in lista_rutas:
        puntero = raiz

        longitud_linea = 0
        for _ in linea:
            longitud_linea += 1

        indice_actual = 0

        for componente in linea:
            if indice_actual == longitud_linea - 1:
                puntero[componente] = True
            else:
                if componente not in puntero:
                    puntero[componente] = {}
                puntero = puntero[componente]

            indice_actual += 1

    print(raiz)


construir_estructura_directorio(entrada)
