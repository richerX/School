# ----------------------------------------------------------------------------
# Поразрядная сортировка | Average O(n + k) | Best O(n + k) --> O(n^2) Worst |
# ----------------------------------------------------------------------------

def BucketSort(mas):
    print("Initial array:")
    print(", ".join(map(str, mas)))    
    for i in range(m):  # Phase
        mas1 = [[] for j in range(10)]
        for j in range(n):  # bucket
            mas1[int(mas[j][m - i - 1])].append(mas[j])
        print("**********")
        print("Phase " + str(i + 1))
        mas = []
        for k in range(10):
            for r in range(len(mas1[k])):
                mas.append(mas1[k][r])
            if mas1[k] != []:
                print("Bucket " + str(k) + ": " + ", ".join(map(str, mas1[k])))
            else:
                print("Bucket " + str(k) + ": empty")
    print("**********")
    print("Sorted array:")
    print(", ".join(map(str, mas)))
