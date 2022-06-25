# ------------------------------------------------------------------------------
# Сортировка выбором максимума | Average O(n^2) | Best O(n^2) --> O(n^2) Worst |
# ------------------------------------------------------------------------------

def SelectionSort(mas):
    for i in range(n):
        min1 = mas[i]
        i1 = i
        for j in range(i, n):
            if mas[j] <= min1:
                min1 = mas[j]
                i1 = j
        mas[i], mas[i1] = mas[i1], mas[i]
