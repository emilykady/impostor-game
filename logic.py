#Categorías que vamos a usar en el juego.
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


#Iniciamos Juego.

#Banner de Bienvenida.
print("¡Bienvenidos al Juego del Impostor!")

#Pedimos el numero de jugadores e iniciamos el array donde guardaremos el orden en el que
#jugarán.
num_Jugadores = int(input("Decirme el Numero de Jugadores que van a participar: "))
Jugadores = []

for i in range(num_Jugadores):
    nombre = input(f"Quien será el Jugador {i+1}")
    Jugadores.append(nombre)


#Hacemos un booleano con el que jugaremos para saber el numero de rondas.
salir = True

#Mientras salir no sea verdadero, hara un random de categoria, impostor y palabra y se hará 
#ronda.
while(salir): 
    categoriaAzar = random.choice(list(categorias_juego.keys()))
    impostor = random.randint(0,num_Jugadores -1)
    palabra = random.choice(categorias_juego[categoriaAzar])

    for i in range(num_Jugadores):
        if(i== impostor ):
            print(f"{Jugadores[i]} Mala Suerte!, eres el impostor, tienes aquí tu pista, úsala como veas " \
            "necesario ;) ")
            print(f"Pista : la categoría es {categoriaAzar}")
            print("\n"*20)
           
        else:
            print(f"{Jugadores[i]} Has tenido suerte esta vez!, NO eres el impostor, Aqui tienes la categoría y palabra!")
            print(f"Pista : la categoría es {categoriaAzar}")
            print(f"la palabra esta ronda es: {palabra}")
            print("\n"*20)
           
    salir=False

        

