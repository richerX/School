# ----------------------------------------------------------------------------
# Сортировка подсчётом | Average O(n + k) | Best O(n + k) --> O(n + k) Worst |
# ----------------------------------------------------------------------------

def CountSort(mas):
    DictionaryNumbers = dict()
    for i in mas:
        try:
            DictionaryNumbers[i] += 1
        except:
            DictionaryNumbers[i] = 1
    answer = []
    keys = list(DictionaryNumbers.keys())
    keys.sort()
    for key in keys:
        answer += [key] * DictionaryNumbers[key]
    return answer
