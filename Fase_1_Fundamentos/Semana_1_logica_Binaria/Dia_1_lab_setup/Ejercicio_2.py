def verificar_exclusiones(patron, ruta):
    letras_ruta = 0
    direccion_ruta = []
    letras_patron = 0
    patron_limpio = ""
    extension_acomparar = ""

    for contar in ruta:
        letras_ruta += 1
        direccion_ruta.append(contar)

    for contar in patron:
        if contar != "*":
            letras_patron += 1
            patron_limpio += contar

    while letras_patron >= 0:
        extension_acomparar = direccion_ruta[letras_ruta - letras_patron]
        letras_patron -= 1

    if extension_acomparar == patron_limpio:
        return True
    else:
        return False


verificar_exclusiones("*.pyc", "fase_1/__pycache__/main.pyc")
