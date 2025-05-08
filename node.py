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

    def send(self, destination, data):
        print(f"[{self.name}] Sending data to {destination.name}...")
        for bit in data:
            print(f"{self.name} ➜ {destination.name} : Bit sent -> {bit}")
            time.sleep(0.3) # Simula retardo de red
        destination.receive(data)

    def receive(self, data):
        print(f"[{self.name}] Received data: {data}")

if __name__ == "__main__":
    nodeA = Node("NodeA")
    nodeB = Node("NodeB")

    traffic = nodeA.generate_traffic(length=10)
    nodeA.send(nodeB, traffic)
