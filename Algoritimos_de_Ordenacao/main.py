'''
Lista de números inteiros: [9, 5, 2, 7, 1, 8, 3, 6, 4].
'''


def Bubble_Sort():
    lista = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    n = len(lista)

    for i in range(n):
        for j in range(n - 1 - i):  # desconsiderando os elementos que já foram lidos .
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)


def Selection_Sort():
    lista = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    n = len(lista)

    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    print(lista)


def Insertion_Sort():
    lista = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    n = len(lista)
    for i in range(1, n):  # ordenção começa à partir do segundo elemento(visualmente) ou indice 1, após o 0
        chave = lista[i] # chave = lista[1]
        j = i - 1  # 'indice anterior'
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    print(lista)


def Shell_Sort():
    lista = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    n = len(lista)
    intervalo = n // 2

    while intervalo > 0:
        for i in range(0, n - intervalo):  # 'Imagine uma lista com 12 elementos, a iteração devera inicar no primeiro e ir até 12 - intervalo, ou seja, 12-6 = 6, a iteraçõ ocorre do primeiro elemento ao 7, após isso ocorre do segundo ao 8 e assim por diante'
            valor = lista[i + intervalo]  # '[1, 2, 3, 4], na primeira iteracao: valor = lista[0 + 2] => lista[2], ou seja, 3'
            j = i  # 'j = primeiro elemento da lista, no caso acima seria j = 1'

            while j >= 0 and lista[j] > valor:
                lista[j + intervalo] = lista[j]  # 'Aqui fazemos a troca dos elementos'
                j -= intervalo
            lista[j + intervalo] = valor
        intervalo //= 2

    print(lista)

if __name__ == '__main__':
    Bubble_Sort()
    Selection_Sort()
    Insertion_Sort()
    Shell_Sort()
