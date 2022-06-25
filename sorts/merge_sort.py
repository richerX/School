# ----------------------------------------------------------------------------------------------
# Сортировка слиянием и слияние | Average O(n*log(n)) | Best O(n*log(n)) --> O(n*log(n)) Worst |
# ----------------------------------------------------------------------------------------------
    
def MergeSort(mas, left, right):
    if len(mas) == 0:
        return
    if right <= left:
        return
    else:
        mid = (right + left) // 2
        MergeSort(mas, left, mid)
        MergeSort(mas, mid + 1, right)
        Merge(mas, left, mid, right)

def Merge(mas, left, mid, right):
    mas1 = []
    i, j = left, mid + 1
    ind = left
    while ind < right + 1:
        if i > mid:
            mas1.append(mas[j])
            j += 1
        elif j > right:
            mas1.append(mas[i])
            i += 1
        elif mas[j] < mas[i]:
            mas1.append(mas[j])
            j += 1
        else:
            mas1.append(mas[i])
            i += 1
        ind += 1
    ind = 0
    for i in range(left, right + 1):
        mas[i] = mas1[ind]
        ind += 1
