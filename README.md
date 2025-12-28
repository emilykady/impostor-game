# El Juego del Impostor

Bienvenido al repositorio del **Juego del Impostor**.  
Los jugadores reciben pistas y palabras secretas según una categoría, mientras uno de ellos es elegido como **impostor** y debe improvisar para no ser descubierto.

---

## Características
- Selección aleatoria de:
  - Categoría (Animales, Ciudades, Países, Comida, etc.)
  - Palabra secreta para los jugadores normales
  - Jugador impostor
- Mensajes diferenciados para impostor y jugadores normales.
- Separación visual entre turnos para ocultar pistas anteriores.
- Flujo de rondas configurable.

---

## Estructura del proyecto
- `categorias_juego`: Diccionario con categorías y listas de palabras.
- Entrada de jugadores por consola.
- Bucle principal que gestiona rondas, pistas y roles.

---

## Cómo jugar
1. Ejecuta el programa:
   ```bash
   python impostor.py
