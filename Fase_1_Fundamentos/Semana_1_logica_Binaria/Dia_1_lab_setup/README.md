Ejercicio 1: Escribe una función llamada segmentar_ruta(cadena_ruta) que reciba un string con una ruta (ejemplo: "fase_1/semana_1/dia_1/script.py") y devuelva una lista de strings con cada uno de los componentes de la ruta.

Restricción algorítmica: No puedes usar str.split('/'). Debes recorrer la cadena carácter por carácter, detectar los delimitadores /, aislar los sub-strings y agregarlos secuencialmente a una lista. Asegúrate de procesar correctamente el último componente si la ruta no termina en /.

Caso de prueba de control: segmentar_ruta("sys/logs/soc/alert.log") debe retornar ["sys", "logs", "soc", "alert.log"].

## resolución del Ejercicio 1 (Motor de Segmentación de Rutas) sin usar split

config:
theme: dark
layout: dagre

---

flowchart TB
Inicio(["INICIO: segmentar_ruta"]) --> Inicializar["Inicializar lista componentes vacía<br>Inicializar acumulador actual vacío"]
Inicializar --> Bucle{"¿Quedan caracteres<br>por leer en la ruta?"}
Bucle -- Sí --> ValidarBarra@{ label: "¿El caracter es<br>igual a '/'?" }
ValidarBarra -- Sí --> VerificarVacio{"¿actual tiene<br>texto acumulado?"}
VerificarVacio -- Sí --> AgregarLista["Agregar actual a componentes<br>Resetear acumulador actual"]
VerificarVacio -- No --> Avanzar["Saltar barra y continuar"]
AgregarLista --> Avanzar
ValidarBarra -- No --> Acumular["Sumar caracter al texto:<br>actual = actual + caracter"]
Acumular --> Avanzar
Avanzar --> Bucle
Bucle -- No --> VerificarUltimo{"¿Quedó texto en<br>actual sin guardar?"}
VerificarUltimo -- Sí --> AgregarUltimo["Agregar residuo de actual<br>a componentes"]
VerificarUltimo -- No --> Retornar["Retornar lista componentes"]
AgregarUltimo --> Retornar
Retornar --> Fin(["FIN DE LA FUNCIÓN"])

    ValidarBarra@{ shape: diamond}
