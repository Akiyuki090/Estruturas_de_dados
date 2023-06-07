'''
Criação de uma lista encadeada simples com todos os métodos
'''

class Node:
    def _init_(self, valor):
        self.valor = valor
        self.next = None

class linkedListSample:
    def _init_(self):
        self.head = None
    
    def insereinicio(self, valor):
        novoValor = Node(valor)
        novoValor.next = self.head
        self.head = novoValor

    def excluiInicio(self):
        if self.head != None:
            self.head = self.head.next
    
    def pesquisaElemento(self, elemento):
        current = self.head
        position = 0
        
        while current != None:
            if current.valor == elemento:
                print(f'Elemento encontrado, posição: {position}')
            else:
                print('Elemento não encontrado')
            current = current.next # nosso incremento
            position += 1 # incrementando para achar a posicao
            
        if self.head == None:
            print('Lista vazia')
            return None
    
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
        
if "__name__"=="__main__":           
    minhaLista = linkedListSample()
    minhaLista.insereinicio(5)
    minhaLista.insereinicio(9)
    minhaLista.insereinicio(8)
    minhaLista.insereinicio(10) # -> é o primeiro da lista
    minhaLista.excluiInicio()
    minhaLista.mostrar()
    minhaLista.pesquisaElemento(5)
    minhaLista.excluiPosicao(2)
    minhaLista.mostrar()
