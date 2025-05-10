

def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio:
        return -1

    if x == l[meio]:
        return meio  # Corrigido para retornar o índice

    if x < l[meio]:
        return busca_binaria(l, x, inicio, meio - 1)
    
    return busca_binaria(l, x, meio + 1, fim)

# Teste da função
l = [1, 3, 5, 7, 9, 11]
alvo = 3
resultado = busca_binaria(l, alvo, 0, len(l) - 1)
print("Índice encontrado:", resultado)