# FASE 5 - EVALUACIÓN FINAL POA
# Problema 4 - Videoteca Digital
#Kevin Cervantes Alviz
#CC: 1233340125


videoteca = [
    ["Interestelar", 2014, 8.7, "Ciencia Ficción"],
    ["Avatar 2", 2022, 7.5, "Acción"],
    ["Titanic", 1997, 8.0, "Drama"],
    ["Top Gun Maverick", 2022, 8.2, "Acción"],
    ["Star Wars: El despertar de la fuerza", 2015, 7.7, "Ciencia Ficción"],
    ["Duna", 2021, 8.0, "Ciencia Ficción"],
    ["Avengers: Endgame", 2019, 8.4, "Acción"],
    ["El Padrino", 1972, 9.2, "Drama"],
    ["El Señor de los Anillos: El Retorno del Rey", 2003, 8.9, "Fantasía"],
    ["android", 2020, 8.9, "Fantasía"],
    ["Michael",2026,7.7,"Docudrama"],
    ["Batman: El caballero de la noche",2008,9.7,"Acción"],
    ["Obsesión",2025,8.2,"Horror psicológico"],
    ["Jack Ryan: Ghost War",2026,5.8,"Acción"],
    ["Proyecto Fin del mundo",2026,8.3,"Aventura Epica"],
    ["Intercambiados",2026,7.3,"Animación"]
]

def contar_titulos(matriz, calificacion_minima, año_limite):

    contador = 0

    for titulo in matriz:

        nombre = titulo[0]
        año = titulo[1]
        calificacion = titulo[2]

        if calificacion >= calificacion_minima and año >= año_limite:
            contador += 1

    return contador


calificacion_minima = 7.0
año_limite = 2020

resultado = contar_titulos(
    videoteca,
    calificacion_minima,
    año_limite
)

print("===================================")
print(" VIDEOTECA DIGITAL ")
print("===================================")

print("Calificación mínima:", calificacion_minima)
print("Año límite:", año_limite)

print("-----------------------------------")
print("Cantidad de títulos encontrados:", resultado)
