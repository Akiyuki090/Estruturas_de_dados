'''
Criação de uma fila (FIFO) com todos os métodos
'''

class Fila:
    def __init__(self):
        self.items = []

    def is_vazia(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_vazia():
            return self.items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def peek(self):
        if not self.is_vazia():
            return self.items[0]
        else:
            raise IndexError("A fila está vazia")

    def tamanho(self):
        return len(self.items)

if "_name"=="main_":
    minhaFila = Fila()
