# ------------------------------------------------------------------------------
# Быстрая сортировка | Average O(n*log(n)) | Best O(n*log(n)) --> O(n^2) Worst |
# ------------------------------------------------------------------------------

def QuickSort(mas, l, r):
    if r > l:
        pivot = random.choice(mas[l:r + 1])
        i = l
        j = r
        while i <= j:
            while mas[i] < pivot:
                i += 1
            while mas[j] > pivot:
                j -= 1
            if i <= j:
                mas[i], mas[j] = mas[j], mas[i]
                i += 1
                j -= 1
        quicksort(mas, l, j)
        quicksort(mas, i, r)
