# red = {"nodo": "gateway", "siguiente": {}}
# cursor = red
# cursor = cursor["siguiente"]
# cursor["nodo"] = {}
# cursor["nodo"] = "siwcht_core"
# cursor["intefaz"] = "eth0"


# print(red)
Lista = ["var", "log"]

raiz = {}


def diccionarios(lista):
    cursor = raiz
    for elementos in lista:

        if elementos not in cursor:
            cursor[elementos] = {}
        cursor = cursor[elementos]
    if "_count" not in cursor:
        cursor["_count"] = 1
    else:
        cursor["_count"] += 1
    print(raiz)


diccionarios(Lista)
