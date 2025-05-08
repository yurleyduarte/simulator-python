import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Definición de la clase Node (Nodo)
class Node:
    def __init__(self, name):
        self.name = name  # El nombre del nodo
        self.traffic = 0  # Aquí almacenamos la cantidad total de tráfico

    def generate_traffic(self, size):
        """Genera una ráfaga de tráfico representado como una cadena de bits"""
        traffic_burst = ''.join(np.random.choice(['0', '1'], size=size))  # Generamos una cadena de bits aleatorios
        self.traffic += size  # Acumulamos el tráfico generado
        return traffic_burst

    def send_traffic(self, other_node, size):
        """Simula el envío de tráfico a otro nodo, enviando bit a bit"""
        traffic_burst = self.generate_traffic(size)  # Genera la ráfaga
        print(f"{self.name} Generated traffic: {traffic_burst}")
        print(f"{self.name} Sending data to {other_node.name}...")

        # Enviar bit por bit
        for bit in traffic_burst:
            print(f"{self.name} ➜ {other_node.name} : Bit sent -> {bit}")
            other_node.receive_traffic(bit)  # El nodo receptor recibe el bit

    def receive_traffic(self, bit):
        """Simula la recepción de tráfico en el nodo, recibe un solo bit"""
        print(f"{self.name} Received data: {bit}")

# Inicializamos dos nodos
node_a = Node("NodeA")
node_b = Node("NodeB")

# Generamos tráfico y lo enviamos
node_a.send_traffic(node_b, 10)  # Nodo A envía 10 bits a Nodo B

# Configuración para la visualización de la simulación de tráfico
fig, ax = plt.subplots()

# Definir el límite de la visualización (coordenadas X y Y)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Crear los puntos que representarán los nodos
node_a_dot, = ax.plot([], [], 'bo', markersize=10, label="NodeA")  # Nodo A
node_b_dot, = ax.plot([], [], 'ro', markersize=10, label="NodeB")  # Nodo B
bit_circle, = ax.plot([], [], 'go', markersize=5)  # Ráfaga de bits

# Crear los textos que mostrarán los nombres y la cantidad de tráfico
node_a_text = ax.text(2, 6, f'{node_a.name}: {node_a.traffic} bits', color="blue", fontsize=12)
node_b_text = ax.text(8, 6, f'{node_b.name}: {node_b.traffic} bits', color="red", fontsize=12)

# Función de inicialización para la animación
def init():
    node_a_dot.set_data([], [])
    node_b_dot.set_data([], [])
    bit_circle.set_data([], [])
    return node_a_dot, node_b_dot, bit_circle, node_a_text, node_b_text

# Función de actualización para la animación
def animate(frame):
    # Establecer las posiciones de los nodos
    node_a_dot.set_data([2], [5])  # Nodo A en (2, 5)
    node_b_dot.set_data([8], [5])  # Nodo B en (8, 5)

    # Simulamos el paso de los bits entre los nodos
    bits_sent = '0011111111'  # Simulación de la secuencia de bits a enviar
    x = np.linspace(2, 8, len(bits_sent))  # Rango de X para la ráfaga de bits
    y = 5 + np.sin(x)  # Forma en Y para la animación (senoidal para suavizar la animación)
    
    # Actualizamos la posición de la ráfaga de bits
    bit_circle.set_data(x[:frame], y[:frame])  # Pasamos una secuencia hasta el frame actual
    
    # Actualizar el texto con la cantidad de tráfico
    node_a_text.set_text(f'{node_a.name}: {node_a.traffic} bits')
    node_b_text.set_text(f'{node_b.name}: {node_b.traffic} bits')

    return node_a_dot, node_b_dot, bit_circle, node_a_text, node_b_text

# Crear la animación
ani = FuncAnimation(fig, animate, frames=10, init_func=init, interval=500, blit=True)

# Guardar la animación como archivo GIF
ani.save("simulacion.gif", writer="magick", fps=2)
ani.save("simulacion.mp4", writer="ffmpeg", fps=2)