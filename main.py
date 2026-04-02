def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos do array
    for i in range(n):
        trocou = False
        # Os últimos i elementos já estão no lugar correto
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        # Se nenhuma troca ocorreu nesta passagem, a lista está ordenada
        if not trocou:
            break
    return arr

# Teste
print("Bubble Sort:", bubble_sort([5, 1, 4, 2]))
