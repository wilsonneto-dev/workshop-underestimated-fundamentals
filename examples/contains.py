import time
import random

tamanho = 100_000_000
lista = list(range(tamanho))
hashset = set(lista)

item = random.randint(0, tamanho - 1)

inicio_lista = time.time()
encontrado_lista = item in lista
tempo_lista = time.time() - inicio_lista

print(f"Verificação na Lista:")
print(f"Encontrado: {encontrado_lista}")
print(f"Tempo: {tempo_lista:.10f} segundos\n")

inicio_conjunto = time.time()
encontrado_conjunto = item in hashset
tempo_conjunto = time.time() - inicio_conjunto

print(f"Verificação no Conjunto:")
print(f"Encontrado: {encontrado_conjunto}")
print(f"Tempo: {tempo_conjunto:.10f} segundos")
