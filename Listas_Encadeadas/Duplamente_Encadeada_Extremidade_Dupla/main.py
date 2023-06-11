'''
Criação de uma lista encadeada com extremidades duplas, com todos os métodos
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeadaED:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

    def inserir_final(self, valor):
        novo_no = No(valor)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no

    def inserir_apos(self, valor, valor_referencia):
        novo_no = No(valor)
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor_referencia:
                if atual == self.fim:
                    self.fim.proximo = novo_no
                    novo_no.anterior = self.fim
                    self.fim = novo_no
                else:
                    novo_no.proximo = atual.proximo
                    novo_no.anterior = atual
                    atual.proximo.anterior = novo_no
                    atual.proximo = novo_no
                return
            atual = atual.proximo
        print("Valor de referência não encontrado na lista.")
			
    def excluir(self, valor):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        atual = self.inicio

        while atual is not None:
            if atual.valor == valor:
                if atual == self.inicio:
                    self.inicio = atual.proximo
                    if self.inicio is not None:
                        self.inicio.anterior = None
                    else:
                        self.fim = None
                elif atual == self.fim:
                    self.fim = atual.anterior
                    if self.fim is not None:
                        self.fim.proximo = None
                    else:
                        self.inicio = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior

                print("Valor excluído:", valor)
                return

            atual = atual.proximo

        print("Valor não encontrado na lista.")

    def mostrar(self):
        if self.inicio is None:
            print("A lista está vazia.")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual.valor, end=" ")
                atual = atual.proximo
            print()

if __name__=="__main__":
	lista = ListaDuplamenteEncadeadaED()
	lista.inserir_inicio(10)
	lista.inserir_inicio(20)
	lista.inserir_final(30)
	lista.inserir_apos(15, 10)
	lista.mostrar()
	lista.excluir(20)
	lista.excluir(30)
	lista.mostrar()
        