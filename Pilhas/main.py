'''
Criação de uma pilha (LIFO) com todos os métodos
'''
class Pilha:
    def __init__(self):
        self.items = []

    def is_vazia(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.is_vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.items)

if __name__ == "__main__":
    minhaPilha = Pilha()
    