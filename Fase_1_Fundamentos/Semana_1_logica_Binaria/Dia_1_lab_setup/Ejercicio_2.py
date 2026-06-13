def verificar_exclusiones(patron, ruta):
    letras_ruta = 0
    direccion_ruta = []
    letras_patron = 0
    patron_limpio = ""
    extension_acomparar = ""
    i = letras_patron
    j = letras_ruta
    for contar in ruta:
        letras_ruta += 1
        direccion_ruta.append(contar)

    for contar in patron:
        if contar != "*":
            letras_patron += 1
            patron_limpio += contar

    while j >= 0:
        if direccion_ruta[i] != patron_limpio[j]:
            return False
        else:
            i -= 1
            j -= 1
            return True


verificar_exclusiones("*.pyc", "fase_1 / __pycache__ / main.pyc")
