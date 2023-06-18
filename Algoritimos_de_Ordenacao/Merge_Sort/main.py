def merge_sort(lista):
    # Condição de parada: se a lista tiver tamanho <= 1, ela já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Divide a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    # Chama recursivamente o merge_sort para ordenar as duas metades
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    # Combina as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Compara os elementos das duas metades e os mescla em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes, se houver, de ambas as metades
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado

# Exemplo de uso
lista = [9, 5, 1, 8, 3, 10, 4, 2, 7, 6]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)
