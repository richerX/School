# --------------------------------------------------------------------
# Сортировка пузырьком | Average O(n^2) | Best O(n) --> O(n^2) Worst |
# --------------------------------------------------------------------

def BubbleSort(mas):
    for i in range(n - 1, 0, -1):
        sens = 0
        for j in range(i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                sens = 1
        if sens == 0:
            break
