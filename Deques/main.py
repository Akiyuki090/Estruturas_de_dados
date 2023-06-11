'''
Criação de um deque (Double queue) com todos os métodos
'''

class Deque:
    def __init__(self):
        self.items = []

    def is_vazio(self):
        return len(self.items) == 0

    def adicionar_inicio(self, elemento):
        self.items.insert(0, elemento)

    def adicionar_fim(self, elemento):
        self.items.append(elemento)

    def remover_inicio(self):
        if not self.is_vazio():
            return self.items.pop(0)
        else:
            raise IndexError("O deque está vazio")

    def remover_fim(self):
        if not self.is_vazio():
            return self.items.pop()
        else:
            raise IndexError("O deque está vazio")

    def tamanho(self):
        return len(self.items)

    def ver_deque(self):
        print(self.items)

if __name__ == "__main__":
    meuDeque = Deque()
