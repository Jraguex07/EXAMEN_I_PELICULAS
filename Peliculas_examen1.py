# Base de datos de películas
peliculas = [
    {"titulo": "The Dark Knight", "genero": "acción", "duracion": "larga", "estilo": "intensa"},
    {"titulo": "Inception", "genero": "acción", "duracion": "larga", "estilo": "compleja"},
    {"titulo": "Mad Max: Fury Road", "genero": "acción", "duracion": "corta", "estilo": "intensa"},
    {"titulo": "Gladiator", "genero": "acción", "duracion": "larga", "estilo": "épica"},
    {"titulo": "John Wick", "genero": "acción", "duracion": "corta", "estilo": "intensa"},
    {"titulo": "Parasite", "genero": "drama", "duracion": "larga", "estilo": "intensa"},
    {"titulo": "The Godfather", "genero": "drama", "duracion": "larga", "estilo": "clásica"},
    {"titulo": "12 Angry Men", "genero": "drama", "duracion": "corta", "estilo": "clásica"},
    {"titulo": "A Beautiful Mind", "genero": "drama", "duracion": "larga", "estilo": "emocional"},
    {"titulo": "The Shawshank Redeemption", "genero": "drama", "duracion": "larga", "estilo": "inspiradora"},
    {"titulo": "La La Land", "genero": "musical", "duracion": "larga", "estilo": "romántica"},
    {"titulo": "The Greatest Showman", "genero": "musical", "duracion": "corta", "estilo": "inspiradora"},
    {"titulo": "Singin' in the Rain", "genero": "musical", "duracion": "corta", "estilo": "clásica"},
    {"titulo": "Inside Out", "genero": "animación", "duracion": "corta", "estilo": "emocional"},
    {"titulo": "Toy Story", "genero": "animación", "duracion": "corta", "estilo": "divertida"},
    {"titulo": "Coco", "genero": "animación", "duracion": "larga", "estilo": "emocional"},
    {"titulo": "Spirited Away", "genero": "animación", "duracion": "larga", "estilo": "fantástica"},
    {"titulo": "Zootopia", "genero": "animación", "duracion": "corta", "estilo": "divertida"},
    {"titulo": "The Grand Budapest Hotel", "genero": "comedia", "duracion": "corta", "estilo": "estilizada"},
    {"titulo": "Superbad", "genero": "comedia", "duracion": "corta", "estilo": "divertida"},
    {"titulo": "Groundhog Day", "genero": "comedia", "duracion": "corta", "estilo": "clásica"},
    {"titulo": "The Big Lebowski", "genero": "comedia", "duracion": "corta", "estilo": "absurda"},
    {"titulo": "Forrest Gump", "genero": "comedia", "duracion": "larga", "estilo": "inspiradora"},
    {"titulo": "Garra", "genero": "accion", "duracion": "larga", "estilo": "divertida"},
]

# Función para recolectar las preferencias del usuario
def obtener_preferencias():
    genero = input("¿Qué género prefieres (acción, drama, animación, musical)? ").lower()
    duracion = input("¿Prefieres películas largas o cortas? ").lower()
    estilo = input("¿Qué estilo prefieres (intensa, emocional, divertida, compleja, clásica, romántica)? ").lower()
    return genero, duracion, estilo

# Función para recomendar una película
def recomendar_pelicula(genero, duracion, estilo):
    recomendaciones = [pelicula["titulo"] for pelicula in peliculas
                       if pelicula["genero"] == genero and
                          pelicula["duracion"] == duracion and
                          pelicula["estilo"] == estilo]
    
    if recomendaciones:
        print("Te recomiendo ver:")
        for recomendacion in recomendaciones:
            print(f"- {recomendacion}")
    else:
        print("Lo siento, no encontré una recomendación que coincida con tus preferencias.")
        repetir = input("¿Quieres intentarlo de nuevo? (si/no): ").lower()
        if repetir == "si":
            main()
        else:
            print("Gracias por usar el sistema de recomendación de películas. ¡Hasta la próxima!")
# Programa principal
def main():
    genero, duracion, estilo = obtener_preferencias()
    recomendacion = recomendar_pelicula(genero, duracion, estilo)
    
    if recomendacion:
        print(f"Te recomiendo ver: {recomendacion}")
    else:
        print("")

if __name__ == "__main__":
    main()
