'''
Criação de uma fila de prioridade com todos os métodos
'''
import heapq

class FilaPrioridade:
    def __init__(self):
        self.heap = []
        self.contador = 0

    def adicionar_elemento(self, elemento, prioridade):
        heapq.heappush(self.heap, (prioridade, self.contador, elemento))
        self.contador += 1

    def remover_elemento(self):
        if self.esta_vazia():
            raise IndexError("A fila de prioridade está vazia")
        return heapq.heappop(self.heap)[2]

    def esta_vazia(self):
        return len(self.heap) == 0
    
if "_name"=="main_":
    # Exemplo de uso
    fila = FilaPrioridade()

    fila.adicionar_elemento("Tarefa 1", 3)
    fila.adicionar_elemento("Tarefa 2", 1)
    fila.adicionar_elemento("Tarefa 3", 2)

    while not fila.esta_vazia():
        elemento = fila.remover_elemento()
        print(elemento)
