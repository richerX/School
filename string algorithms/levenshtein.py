def levenshtein_distance(a, b):
    answer = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        answer[i][0] = i
    for j in range(len(b) + 1):
        answer[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                answer[i][j] = answer[i - 1][j - 1]
            else:
                num1 = answer[i - 1][j]
                num2 = answer[i][j - 1]
                num3 = answer[i - 1][j - 1]
                answer[i][j] = min(num1, num2, num3) + 1
    return answer[len(a)][len(b)]
