
def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

# Pede os números ao usuário
entrada = input("Digite os números separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Ordena a lista
bubble_sort(lista)
print("Lista ordenada:", lista)