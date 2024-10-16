# Trabajo de Luciana Sosa

# CircleCI

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-lgsosa/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-lgsosa/tree/main)

# Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/28f89d87fb4e58907aa5/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-lgsosa/maintainability)

# Test Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/28f89d87fb4e58907aa5/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-lgsosa/test_coverage)



<h1 style="text-align:center; color:#3498db;">Juego de Ajedrez en Python</h1>


## Introducción

Este documento detalla el proceso de desarrollo de un juego de Ajedrez en Python, siguiendo las reglas y características descritas en el artículo de Wikipedia sobre Ajedrez. El juego se implementará en una interfaz de consola, permitiendo a los jugadores disfrutar de partidas de Ajedrez en un entorno virtual.


### 1. Jugabilidad
Los jugadores deben poder mover sus piezas según las reglas de movimiento específicas para cada tipo de pieza.

### 2. Fin del juego
El juego debe finalizar cuando:
- Un jugador se queda sin piezas.
- Los jugadores deciden terminar la partida de mutuo acuerdo (empate).

## Procedimiento para Instalar y Ejecutar el Juego

### 1. Requisitos previos
Para poner en funcionamiento el juego de ajedrez en modo de testing y modo desplegado con Docker, necesitas tener instalados los siguientes componentes:
- Docker
- Python 3.x

### 2. Clonar el repositorio
Primero, clona el repositorio oficial del juego de Ajedrez:
```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-lgsosa.git
```
Luego, navega al directorio del proyecto:

### 3. Construir la imagen de Docker
Para construir la imagen de Docker, ejecuta el siguiente comando en la raíz del proyecto:
```bash
docker buildx build -t ajedrez-2024-lgsosa .
```

### 4. Ejecutar el contenedor de Docker
Después de construir la imagen, ejecuta el contenedor con el siguiente comando:
```bash
docker run -i ajedrez-2024-lgsosa
```

Este comando iniciará el juego de Ajedrez en la consola. Sigue las instrucciones que aparecen para comenzar una partida.

## 3. Jugabilidad

Cada jugador alterna turnos para mover una pieza por turno de acuerdo a las siguientes reglas de movimiento:

- **Rey**: Se mueve exactamente una casilla en cualquier dirección: horizontal, vertical o diagonal. Movimiento especial: Enroque (el rey se mueve dos casillas hacia una torre, y la torre se mueve a la casilla adyacente al rey).
  
- **Reina**: Se mueve cualquier número de casillas en cualquier dirección: horizontal, vertical o diagonal.

- **Torre**: Se mueve cualquier número de casillas en dirección horizontal o vertical. No puede saltar sobre otras piezas. Movimiento especial: Enroque (involucra al rey).

- **Alfil**: Se mueve cualquier número de casillas en dirección diagonal. No puede saltar sobre otras piezas.

- **Caballo**: Se mueve en forma de "L": dos casillas en una dirección y luego una casilla perpendicular, o una casilla en una dirección y dos casillas perpendiculares. Los caballos pueden saltar sobre otras piezas.

- **Peón**: Se mueve hacia adelante una casilla. En su primer movimiento, un peón puede avanzar dos casillas. Los peones capturan en diagonal. Movimientos especiales: En passant (un peón puede capturar a otro peón enemigo que haya avanzado dos casillas en su primer movimiento, como si hubiera avanzado solo una) y promoción (cuando un peón alcanza la última fila del oponente, puede ser promovido a cualquier otra pieza, usualmente una reina).
