def calcular_temperatura_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Argumentos:
    datos (dict): Un diccionario donde las claves son nombres de ciudades y los valores son listas de listas
                  donde cada sublista representa las temperaturas de una semana.

    Retorna:
    dict: Un diccionario donde las claves son nombres de ciudades y los valores son las temperaturas promedio
          de cada ciudad.
    """
    temperatura_promedio_por_ciudad = {}

    for ciudad, semanas in datos.items():
        total_temperaturas = 0
        total_horas = 0
        for semana in semanas:
            total_temperaturas += sum(semana)
            total_horas += len(semana)
        temperatura_promedio = total_temperaturas / total_horas
        temperatura_promedio_por_ciudad[ciudad] = temperatura_promedio

    return temperatura_promedio_por_ciudad

# Ejemplo de uso:
datos = {
    'ESMERALDA': [
        [20, 22, 19, 25, 23],
        [21, 23, 20, 24, 22],
        [19, 24, 18, 22, 20],
        [22, 25, 21, 26, 24]
    ],
    'Ciudad LOJA': [
        [18, 20, 17, 23, 21],
        [19, 21, 18, 22, 20],
        [17, 22, 16, 20, 18],
        [20, 23, 19, 24, 22]
    ],
    'Ciudad MANABI': [
        [22, 24, 21, 27, 25],
        [23, 25, 22, 26, 24],
        [21, 26, 20, 24, 22],
        [24, 27, 23, 28, 26]
    ]
}

temperatura_promedio = calcular_temperatura_promedio(datos)
for ciudad, promedio in temperatura_promedio.items():
    print(f"Temperatura promedio de {ciudad}: {promedio:.2f}")
