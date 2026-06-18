def verificar_exclusiones(patron, ruta):

    largo_ruta = 0
    for caracter in ruta:
        largo_ruta += 1

    largo_patron = 0
    for caracter in patron:
        largo_patron += 1

    i = largo_patron - 1
    j = largo_ruta - 1

    while i >= 0 and j >= 0:
        if patron[i] == "*":
            while j > 0 and ruta[j] != "/":
                j -= 1
            i -= 1
        else:
            if patron[i] != ruta[j]:
                return False
            i -= 1
            j -= 1
    if j < 0 and i >= 0:
        return False

    if i < 0 and j >= 0:
        return False

    return True


# Debe dar False (Prefijo no coincide)
print(verificar_exclusiones("logs/*.pyc", "/vacio/logs/main.pyc"))
