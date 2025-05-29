Simulación de Red en Python
Este proyecto es una simulación sencilla de una red en Python, que permite modelar la transmisión de una ráfaga de bits entre nodos a través de enlaces configurables. El objetivo es ilustrar conceptos básicos como nodos, generación de tráfico, ancho de banda, tasa de transferencia, y retardo.

🎯 Propósito

Este programa busca simular el comportamiento de una red básica donde:

•	Los nodos generan ráfagas de bits (tráfico).

•	Los enlaces conectan nodos y simulan la transmisión de datos considerando limitaciones reales como el ancho de banda y el retardo.

•	Se calcula el retardo total y se guarda un registro detallado de la simulación en un archivo de texto.

Es útil para fines educativos, especialmente para estudiantes de redes de computadoras o cursos de simulación de sistemas.
________________________________________
⚙️ Cómo funciona

Estructura Principal
1. Clase Node
   
  Representa un nodo de red.

  •	__init__(name): Inicializa el nodo con un nombre.
  
  •	generate_traffic(length): Genera una ráfaga de bits aleatorios de la longitud especificada.
  
  •	receive(data): Imprime los datos que el nodo ha recibido.
  
2. Clase Enlace
   
Representa un enlace de comunicación entre dos nodos.

•	__init__(source, destination, bandwidth, transfer_rate, delay): Configura el enlace con nodo origen, nodo destino, ancho de banda (bits por bloque), tasa de transferencia (bps), y retardo (s).

•	transmit(data, log_lines): Divide los datos en bloques según el ancho de banda y los transmite simulando el tiempo necesario. Se registra cada evento en log_lines.

3. Función main()
   
Coordina todo el proceso de la simulación:
  1.	Solicita al usuario:
        •	Número de nodos y sus nombres automáticos (nodo 1, nodo 2, ...).
    
        •	Número de enlaces a configurar.
        
        •	Parámetros de cada enlace (nodo origen, destino, ancho de banda, tasa de transferencia, y retardo).
        
        •	Nodo que generará la ráfaga de bits.
        
        •Longitud de la ráfaga.
  
2.	Genera la ráfaga de bits en el nodo seleccionado.
3.	Transmite los datos secuencialmente por todos los enlaces definidos.
4.	Guarda un registro completo de la simulación en un archivo llamado simulacion_resultado.txt.
________________________________________
📝 Ejemplo de uso

Al ejecutar el programa, se solicita al usuario la configuración de la red mediante entrada por consola. Luego, el programa realiza la transmisión simulada y muestra mensajes como:

    [Enlace] nodo 1 ➜ nodo 2
    Detalles del enlace: Ancho de banda = 4 bits, Tasa de transferencia = 2.0 bps, Retardo = 0.5 s
    [nodo 1] Enviando bloque: 1010
    [Enlace] Transmitiendo 4 bits con retardo total: 2.500s
    [nodo 2] Received data: 10101011

📂 Salida

El resultado de la simulación se almacena en el archivo simulacion_resultado.txt, que contiene:

•	La ráfaga generada.

•	Información de cada enlace.

•	Bloques transmitidos y sus retardos individuales.

•	Retardo total acumulado.
________________________________________
✅ Requisitos

•	Python 3.x
•	No se requiere instalar bibliotecas externas (random, time y funciones estándar de entrada/salida son utilizadas).
________________________________________
🚀 Ejecución

python simulador_red.py

🧠 Conceptos aplicados

•	Simulación por software de procesos de red.

•	Manejo de retardos y segmentación de datos.

•	Uso de programación orientada a objetos en Python.
