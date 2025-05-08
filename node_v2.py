import random
import time

class Node:
    def __init__(self, name):
        self.name = name

    def generate_traffic(self, length=8):
        # Genera una ráfaga de bits aleatoria
        burst = ''.join(random.choice(['0', '1']) for _ in range(length))
        print(f"[{self.name}] Generated traffic: {burst}")
        return burst

    def receive(self, data):
        print(f"[{self.name}] Received data: {data}")

class Enlace:
    def __init__(self, bandwidth, transfer_rate, delay):
        """
        bandwidth: int - cantidad máxima de bits por ráfaga
        transfer_rate: float - bits por segundo
        delay: float - retardo fijo en segundos
        """
        self.bandwidth = bandwidth
        self.transfer_rate = transfer_rate
        self.delay = delay

    def transmit(self, source, destination, data):
        print(f"\n[Enlace] {source.name} ➜ {destination.name}")
        
        # Aplicar ancho de banda
        data_chunks = [data[i:i+self.bandwidth] for i in range(0, len(data), self.bandwidth)]

        for chunk in data_chunks:
            print(f"[{source.name}] Enviando bloque: {chunk}")
            # Calcular tiempo por chunk según tasa de transferencia
            time_to_send = len(chunk) / self.transfer_rate
            total_delay = time_to_send + self.delay
            print(f"[Enlace] Transmitiendo {len(chunk)} bits con retardo total: {total_delay:.3f}s")
            time.sleep(total_delay)

        destination.receive(data)

# Simulación con múltiples nodos
if __name__ == "__main__":
    #Nodos
    nodeA = Node("NodeA")
    nodeB = Node("NodeB")
    nodeC = Node("NodeC")

    # Enlace 1 con ancho de banda de 5 bits, tasa 10 bps, retardo de 0.5s
    # Enlace 2 con ancho de banda de 4 bits, tasa 8 bps, retardo de 1s
    enlace1 = Enlace(bandwidth=5, transfer_rate=10, delay=0.5)
    enlace2 = Enlace(bandwidth=4, transfer_rate=8, delay=1)

    # Generar tráfico
    traffic = nodeA.generate_traffic(length=12)

    # Transmisión entre nodos usando enlaces configurados
    enlace1.transmit(nodeA, nodeB, traffic)
    enlace2.transmit(nodeB, nodeC, traffic)

