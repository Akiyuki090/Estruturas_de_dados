'''
Criação de um vetor ordenado com todos os métodos
'''

class vetor_ordenado:
    def _init_(self):
        self.vetor = []
    
    def adicionarElemento(self, elemento):
        posicao = 0
        while posicao < len(self.vetor) and self.vetor[posicao] < elemento:
            posicao += 1
        self.vetor.append(None)
        for i in range(len(self.vetor) - 1, posicao, -1):
            self.vetor[i] = self.vetor[i - 1]
        self.vetor[posicao] = elemento
    
    def pesquisaElemento(self, elemento):
        for i in range(len(self.vetor)):
            if self.vetor[i] == elemento:
                print(f'Valor encontrado na posição: {i}')
            elif self.vetor[i] > elemento:
                print(f'Valor: {elemento} não encontrado no vetor ordenado')
    
    def excluiElemento(self, elemento):
        if elemento in self.vetor:
            self.vetor.remove(elemento)
            print(f'O valor {elemento} foi removido com sucesso !!!')
        else:
            print(f'O valor {elemento} não foi encontrado na lista !!!')

    def verVetor(self):
        print(self.vetor)

if "_name"=="main_":
    meuVetor = vetor_ordenado()
    