'''
Criação de um vetor não ordenado com todos os métodos
'''

class VetorNaoOrdenado:
    def __init__(self):
        self.vetor = []

    def adicionar_elemento(self, elemento):
        self.vetor.append(elemento)

    def inserir_elemento(self, elemento, posicao):
        self.vetor.insert(posicao, elemento)

    def imprimir_elementos(self):
        for elemento in self.vetor:
            print(elemento)

    def pesquisa_linear(self, elemento):
        for i in range(len(self.vetor)):
            if self.vetor[i] == elemento:
                return i  # Retorna o índice onde o elemento foi encontrado
        return -1  # Retorna -1 se o elemento não foi encontrado

    def remover_elemento(self, elemento):
        indice = self.pesquisa_linear(elemento)  # Verifica se o elemento está presente no vetor
        if indice != -1:
            del self.vetor[indice]  # Remove o elemento do vetor
            print("Elemento removido com sucesso!")
        else:
            print("Elemento não encontrado.")

if "__name__"=="__main__":
    meu_vetor = VetorNaoOrdenado()
    meu_vetor.adicionar_elemento(5)
    meu_vetor.adicionar_elemento(2)
    meu_vetor.adicionar_elemento(3)
    meu_vetor.adicionar_elemento(5)
    meu_vetor.inserir_elemento(12, 4)
    meu_vetor.pesquisa_linear(12)
    meu_vetor.remover_elemento(4)
