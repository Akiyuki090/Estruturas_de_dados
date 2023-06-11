'''
Crianda uma recursão
'''
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)
