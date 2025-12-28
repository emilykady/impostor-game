import random

categorias_juego = {
    "Animales": ["Perro", "Gato", "Loro", "Elefante", "Tigre", "Caballo", "Delfín", "Águila", "Serpiente", "Conejo"],
    "Ciudades": ["Madrid", "Barcelona", "Berlín", "Viena", "Tokio", "Nueva York", "Buenos Aires", "Roma", "París", "Londres"],
    "Países": ["España", "Alemania", "México", "Argentina", "Japón", "Italia", "Francia", "Brasil", "Canadá", "Australia"],
    "Comida": ["Pizza", "Hamburguesa", "Paella", "Sushi", "Tacos", "Arepa", "Ceviche", "Croissant", "Ramen", "Empanada"],
    "Colores": ["Rojo", "Azul", "Verde", "Amarillo", "Negro", "Blanco", "Morado", "Naranja", "Rosa", "Gris"],
    "Deportes": ["Fútbol", "Baloncesto", "Tenis", "Natación", "Atletismo", "Ciclismo", "Boxeo", "Rugby", "Golf", "Voleibol"],
    "Profesiones": ["Doctor", "Ingeniero", "Profesor", "Abogado", "Carpintero", "Músico", "Actor", "Cocinero", "Arquitecto", "Piloto"],
    "Tecnología": ["Ordenador", "Teléfono", "Tablet", "Internet", "Robot", "Dron", "Consola", "Teclado", "Ratón", "Servidor"],
    "Películas": ["Matrix", "Titanic", "Avatar", "Inception", "Gladiator", "Toy Story", "Star Wars", "Jurassic Park", "Frozen", "El Padrino"],
    "Instrumentos": ["Guitarra", "Piano", "Violín", "Batería", "Flauta", "Saxofón", "Trompeta", "Arpa", "Ukelele", "Acordeón"]
}
print("¡Bienvenidos al Juego del Impostor!")

num_Jugadores = 0
while num_Jugadores < 3:
    try:
        num_Jugadores = int(input("Decirme el número de jugadores (mínimo 3): "))
        if num_Jugadores < 3:
            print("Error: Deben ser al menos 3 jugadores.")
    except ValueError:
        print("Por favor, introduce un número válido.")


Jugadores = []
for i in range(num_Jugadores):
    nombre = input(f"¿Quién será el Jugador {i+1}?: ")
    Jugadores.append(nombre)


num_rondas = int(input("¿Cuántas rondas de frases queréis hacer? (Ejemplo: 3): "))

def ronda(JugadoresRespuesta):
    for i in range(len(Jugadores)):
        res = input(f"\nTurno de {Jugadores[i]}. Escribe tu frase: ")
        JugadoresRespuesta[Jugadores[i]] = res

# Inicio del juego
salir = True
while salir:
    # Selección aleatoria de palabra e impostor [cite: 36, 37]
    palabra_jugador = random.choice(list(categorias_juego.keys()))
    pista_impostor = categorias_juego[palabra_jugador]
    impostor = random.randint(0, num_Jugadores - 1)

    # Reparto de información [cite: 38, 40]
    for i in range(num_Jugadores):
        input(f"\n{Jugadores[i]}, pulsa Enter para ver tu secreto...")
        if i == impostor:
            print(f"¡Mala suerte, eres el impostor!, Tu pista es: {pista_impostor}")
        else:
            print(f"¡Buena suerte, no eres el impostor!, La palabra secreta es: {palabra_jugador}")
        
        input("Pulsa Enter para borrar la pantalla y pasar al siguiente...")
        print("\n" * 50)

 
    JugadoresRespuesta = {}
    for r in range(num_rondas):
        print(f"--- Ronda {r+1} ---")
        ronda(JugadoresRespuesta)
        print("\nRespuestas acumuladas:")
        for jugador, respuesta in JugadoresRespuesta.items():
            print(f"- {jugador}: {respuesta}")


    print("\n--- FASE DE VOTACIÓN ---")
    votos_impostor = 0
    votos_no_impostor = 0
    
    for i in range(num_Jugadores):
        while True:
            voto = input(f"{Jugadores[i]}, ¿quién crees que es el impostor?: ")
            if voto == Jugadores[i]: 
                print("No puedes votarte a ti mismo. Elige a otro.")
            elif voto in Jugadores:
                break
            else:
                print("Ese jugador no existe. Escribe el nombre correctamente.")
        
        if voto == Jugadores[impostor]:
            votos_impostor += 1
        else:
            votos_no_impostor += 1

    print("\n--- RESULTADO FINAL ---")
    if votos_impostor > votos_no_impostor:
        print(f"Felicidades! Habéis descubierto al impostor: {Jugadores[impostor]}")
        print(f"La palabra secreta era: {palabra_jugador}")
    else:
        print(f"Mala Suerte! El impostor ha ganado. Era: {Jugadores[impostor]}")
        print(f"La palabra del impostor era '{pista_impostor}' y la vuestra '{palabra_jugador}'")

    continuar = input("\n¿Queréis jugar otra partida? (si/no): ").lower()
    if continuar != "si":
        salir = False

print("¡Gracias por jugar!")