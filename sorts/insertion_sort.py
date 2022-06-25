# --------------------------------------------------------------------
# Сортировка вставками | Average O(n^2) | Best O(n) --> O(n^2) Worst |
# --------------------------------------------------------------------

def InsertionSort(mas):
    for i in range(1, n):
        elem = mas[i]
        while i - 1 >= 0 and mas[i - 1] > elem:
            mas[i] = mas[i - 1]
            i -= 1
        mas[i] = elem
