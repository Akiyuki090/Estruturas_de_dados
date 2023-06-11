'''
Criação de uma lista encadeada simples com todos os métodos
'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class linkedListSample:
    def __init__(self):
        self.head = None
    
    def insereInicio(self, valor):
        novoValor = Node(valor)
        novoValor.next = self.head
        self.head = novoValor

    def excluiInicio(self):
        if self.head != None:
            self.head = self.head.next # só se a lista n estiver vazia
        else:
            print('Lista vazia !') 
        
    def pesquisaElemento(self, elemento):
        current = self.head
        position = 0
        
        while current != None:
            if current.valor == elemento:
                print(f'Elemento encontrado, posição: {position}')
                return
            current = current.next # incremento
            position += 1 # incremento para achar a posição
            
        print('Elemento não encontrado')
    
    def excluiPosicao(self, posicao):
        if posicao < 0 or self.head is None:
            print('Posição inválida ou lista vazia')
            return
        if posicao == 0:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head
        count = 0

        while current != None and count < posicao:
            previous = current
            current = current.next
            count += 1
        if current != None:
            previous.next = current.next
           
    def mostrar(self):
        current = self.head
        while current != None:
            print(current.valor, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    minhaLista = linkedListSample()
    minhaLista.insereInicio(5)
    minhaLista.insereInicio(9)
    minhaLista.insereInicio(8)
    minhaLista.insereInicio(10) # -> é o primeiro da lista
    minhaLista.mostrar()
    minhaLista.excluiInicio()
    minhaLista.mostrar()
    minhaLista.pesquisaElemento(5)
    minhaLista.excluiPosicao(2)
    minhaLista.mostrar()
