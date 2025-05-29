import random
import time

class Node:
    def __init__(self, name):
        self.name = name

    def generate_traffic(self, length=8):
        burst = ''.join(random.choice(['0', '1']) for _ in range(length))
        print(f"[{self.name}] Generated traffic: {burst}")
        return burst

    def receive(self, data):
        print(f"[{self.name}] Received data: {data}")

class Enlace:
    def __init__(self, source, destination, bandwidth, transfer_rate, delay):
        self.source = source
        self.destination = destination
        self.bandwidth = bandwidth
        self.transfer_rate = transfer_rate
        self.delay = delay

    def transmit(self, data, log_lines):
        print(f"\n[Enlace] {self.source.name} ➜ {self.destination.name}")
        log_lines.append(f"\n[Enlace] {self.source.name} ➜ {self.destination.name}")
        
        print(f"Detalles del enlace: Ancho de banda = {self.bandwidth} bits, Tasa de transferencia = {self.transfer_rate} bps, Retardo = {self.delay} s")
        log_lines.append(f"Detalles del enlace: Ancho de banda = {self.bandwidth} bits, Tasa de transferencia = {self.transfer_rate} bps, Retardo = {self.delay} s")

        data_chunks = [data[i:i+self.bandwidth] for i in range(0, len(data), self.bandwidth)]
        total_delay_sum = 0  # Acumulador del retardo total

        for chunk in data_chunks:
            print(f"[{self.source.name}] Enviando bloque: {chunk}")
            time_to_send = len(chunk) / self.transfer_rate
            total_delay = time_to_send + self.delay
            total_delay_sum += total_delay
            print(f"[Enlace] Transmitiendo {len(chunk)} bits con retardo total: {total_delay:.3f}s")
            time.sleep(total_delay)

            log_lines.append(f"[{self.source.name}] Enviando bloque: {chunk}")
            log_lines.append(f"[Enlace] Transmitiendo {len(chunk)} bits con retardo total: {total_delay:.3f}s")

        self.destination.receive(data)
        log_lines.append(f"[{self.destination.name}] Received data: {data}")
        log_lines.append(f"Retardos individuales acumulados: {len(data_chunks)} bloques transmitidos.")
        log_lines.append(f"Retardo total acumulado: {total_delay_sum:.3f} segundos")
        print(f"Retardo total acumulado: {total_delay_sum:.3f} segundos")

def main():
    print("=== Simulación de Envío de Ráfagas de Bits ===\n")
    log_lines = []

    # Validar número de nodos
    while True:
        try:
            num_nodes = int(input("¿Cuántos nodos deseas crear?: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero.")

    nodes = []
    for i in range(num_nodes):
        name = f"nodo {i+1}"
        nodes.append(Node(name))

    print("\nNodos creados:")
    for idx, node in enumerate(nodes):
        print(f"  [{idx}] {node.name}")

    # Validar número de enlaces
    while True:
        try:
            num_links = int(input("\n¿Cuántos enlaces deseas configurar?: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero.")

    enlaces = []
    for i in range(num_links):
        print(f"\n--- Enlace {i+1} ---")
        for idx, node in enumerate(nodes):
            print(f"  [{idx}] {node.name}")
        
        # Validar índice del nodo origen
        while True:
            try:
                source_idx = int(input("Selecciona el índice del nodo **origen**: "))
                break
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        # Validar índice del nodo destino
        while True:
            try:
                dest_idx = int(input("Selecciona el índice del nodo **destino**: "))
                break
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        
        # Validar ancho de banda (solo enteros)
        while True:
            try:
                bw = int(input("Ancho de banda (bits por bloque): "))
                break
            except ValueError:
                print("Error: No se aceptan decimales ni letras. Ingresa un número entero.")

        # Validar tasa de transferencia
        while True:
            try:
                rate = float(input("Tasa de transferencia (bits por segundo): "))
                break
            except ValueError:
                print("Error: Ingresa un número válido (puede tener decimales).")

        # Validar retardo
        while True:
            try:
                delay = float(input("Retardo (segundos): "))
                break
            except ValueError:
                print("Error: Ingresa un número válido (puede tener decimales).")

        enlaces.append(Enlace(nodes[source_idx], nodes[dest_idx], bw, rate, delay))

    # Nodo que generará el tráfico
    print("\nSelecciona el nodo que generará la ráfaga:")
    for idx, node in enumerate(nodes):
        print(f"  [{idx}] {node.name}")

    while True:
        try:
            traffic_node_idx = int(input("Índice del nodo generador: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero.")

    # Validar longitud de la ráfaga
    while True:
        try:
            burst_length = int(input("Longitud de la ráfaga de bits: "))
            break
        except ValueError:
            print("Error: Ingresa un número entero.")

    data = nodes[traffic_node_idx].generate_traffic(burst_length)
    log_lines.append(f"[{nodes[traffic_node_idx].name}] Generated traffic: {data}")

    # Transmitir los datos por todos los enlaces en orden
    current_data = data
    for enlace in enlaces:
        enlace.transmit(current_data, log_lines)

    # Guardar resultado
    with open("simulacion_resultado.txt", "w") as file:
        for line in log_lines:
            file.write(line + "\n")

    print("Simulación finalizada. Resultado guardado en 'simulacion_resultado.txt'.")


if __name__ == "__main__":
    main()


