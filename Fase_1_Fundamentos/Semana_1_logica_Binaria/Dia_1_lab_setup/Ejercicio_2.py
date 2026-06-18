def verificar_exclusiones(patron, ruta):

    largo_ruta = 0
    for caracter in ruta:
        largo_ruta += 1

    patron_limpio = ""
    largo_patron = 0
    for caracter in patron:
        if caracter != "*":
            largo_patron += 1
            patron_limpio += caracter

    i = largo_patron - 1
    j = largo_ruta - 1

    while i >= 0 and j >= 0:
        if ruta[j] != patron_limpio[i]:
            return False
        i -= 1
        j -= 1

    return True


print(verificar_exclusiones("efghefgh", "efgh"))
print(verificar_exclusiones("infraestructura/fadena/seguridad/logs/*.pyc", "main.pyc"))
