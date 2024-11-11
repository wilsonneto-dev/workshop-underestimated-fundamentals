import random

def busca_linear(lista, item):
    iteracoes = 0
    for elemento in lista:
        iteracoes += 1
        if elemento == item:
            return True, iteracoes
    return False, iteracoes


def busca_binaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    iteracoes = 0
    while esquerda <= direita:
        iteracoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return True, iteracoes
        elif lista[meio] < item:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False, iteracoes


tamanho_lista = 1000000
lista = list(range(tamanho_lista))
item = random.randint(0, tamanho_lista - 1)

encontrado_linear, iteracoes_linear = busca_linear(lista, item)
print(f"Busca Linear - Encontrado: {encontrado_linear}, Iterações: {iteracoes_linear}")

encontrado_binaria, iteracoes_binaria = busca_binaria(lista, item)
print(f"Busca Binária - Encontrado: {encontrado_binaria}, Iterações: {iteracoes_binaria}")


tamanhos = [10, 100, 1000, 10000, 100000, 1000000]
iteracoes_linear = []
iteracoes_binaria = []

for tamanho in tamanhos:
    lista = list(range(tamanho))
    item = lista[-1]  # Pior caso para busca linear

    _, iter_lin = busca_linear(lista, item)
    _, iter_bin = busca_binaria(lista, item)

    print(f"---\nLista de tamanho {tamanho}")
    print(f"Busca Linear - Iterações: {iter_lin}")
    print(f"Busca Binária - Iterações: {iter_bin}")

